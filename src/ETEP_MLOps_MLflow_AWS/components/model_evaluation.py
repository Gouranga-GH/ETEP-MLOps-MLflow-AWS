import os  # For interacting with the operating system, such as file operations
import pandas as pd  # For data manipulation
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score  # For calculating evaluation metrics
from urllib.parse import urlparse  # For parsing URLs
import mlflow  # For MLflow tracking and model management
import mlflow.sklearn  # For logging scikit-learn models with MLflow
import numpy as np  # For numerical operations
import joblib  # For loading saved models
from src.ETEP_MLOps_MLflow_AWS.entity.config_entity import ModelEvaluationConfig  # Importing ModelEvaluationConfig class
from src.ETEP_MLOps_MLflow_AWS.utils.common import save_json  # Importing a utility function for saving JSON data
from pathlib import Path  # For handling file system paths

# Definition of the ModelEvaluation class
class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        # Initializing the class with a ModelEvaluationConfig object
        self.config = config

    # Method to evaluate metrics
    def eval_metrics(self, actual, pred):
        # Calculate root mean squared error (RMSE)
        rmse = np.sqrt(mean_squared_error(actual, pred))
        # Calculate mean absolute error (MAE)
        mae = mean_absolute_error(actual, pred)
        # Calculate R-squared score
        r2 = r2_score(actual, pred)
        # Return the calculated metrics
        return rmse, mae, r2

    # Method to log metrics and model into MLflow
    def log_into_mlflow(self):
        # Load test data and the trained model
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        # Separate features and target variable from the test data
        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        # Set MLflow tracking URI for logging
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        # Start a new MLflow run
        with mlflow.start_run():
            # Predict on the test data using the loaded model
            predicted_qualities = model.predict(test_x)

            # Calculate metrics for the predictions
            rmse, mae, r2 = self.eval_metrics(test_y, predicted_qualities)

            # Save metrics as a JSON file locally
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            # Log parameters and metrics to MLflow
            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)

            # Register the model with MLflow if not using a file store for tracking
            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticnetModel")
            else:
                mlflow.sklearn.log_model(model, "model")
