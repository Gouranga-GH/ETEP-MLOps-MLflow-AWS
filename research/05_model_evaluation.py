# Importing necessary libraries
import os  # For directory operations
import pandas as pd  # For data manipulation
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score  # For evaluating the model
from urllib.parse import urlparse  # For parsing URLs
import mlflow  # For logging and tracking experiments
import mlflow.sklearn  # For logging sklearn models in MLflow
import numpy as np  # For numerical operations
import joblib  # For loading saved models

# Displaying the current working directory
print(os.getcwd())

# Changing the directory to one level up
os.chdir("../")

# Displaying the new current working directory
print(os.getcwd())

# Setting environment variables for MLflow
os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/Gouranga-GH/ETEP-MLOps-MLflow-AWS.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "Gouranga-GH"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "798003b0394763ed4834398be1cfc32f50ea36f1"

# Defining a frozen dataclass to hold configuration for model evaluation
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path  # Root directory for storing evaluation artifacts
    test_data_path: Path  # Path to the test data CSV file
    model_path: Path  # Path to the trained model file
    all_params: dict  # Parameters used in the model
    metric_file_name: Path  # File name to save evaluation metrics
    target_column: str  # Name of the target column in the dataset
    mlflow_uri: str  # MLflow tracking URI

# Importing custom constants and utility functions
from src.ETEP_MLOps_MLflow_AWS.constants import *
from src.ETEP_MLOps_MLflow_AWS.utils.common import read_yaml, create_directories, save_json

# Configuration manager class to handle reading configurations and setting up directories
class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH, schema_filepath=SCHEMA_FILE_PATH):
        # Reading configurations from YAML files
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        # Creating necessary directories for artifacts
        create_directories([self.config.artifacts_root])

    # Function to get model evaluation configuration settings
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN

        # Creating directories based on configuration
        create_directories([config.root_dir])

        # Initializing the ModelEvaluationConfig object with necessary paths and settings
        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path=config.model_path,
            all_params=params,
            metric_file_name=config.metric_file_name,
            target_column=schema.name,
            mlflow_uri="https://dagshub.com/Gouranga-GH/ETEP-MLOps-MLflow-AWS.mlflow",
        )

        return model_evaluation_config

# Model evaluation class to handle model testing, metric calculation, and logging to MLflow
class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config  # Storing the configuration object

    # Function to compute evaluation metrics
    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))  # Root Mean Squared Error
        mae = mean_absolute_error(actual, pred)  # Mean Absolute Error
        r2 = r2_score(actual, pred)  # R-squared value
        return rmse, mae, r2

    # Function to log evaluation metrics and model details into MLflow
    def log_into_mlflow(self):
        # Loading the test data and trained model
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        # Splitting the test data into features (X) and target (y)
        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        # Setting the MLflow tracking URI
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        # Starting an MLflow run for logging
        with mlflow.start_run():
            # Making predictions using the trained model
            predicted_qualities = model.predict(test_x)

            # Calculating evaluation metrics
            (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)

            # Saving metrics locally as JSON
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            # Logging parameters and metrics to MLflow
            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)

            # Registering the model in MLflow, depending on the tracking URI type
            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticnetModel")
            else:
                mlflow.sklearn.log_model(model, "model")

# Main execution block to run the model evaluation process
if __name__ == "__main__":
    try:
        # Initializing configuration manager and getting model evaluation configuration
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()

        # Creating a ModelEvaluation object and running the evaluation and logging process
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()
    except Exception as e:
        # Handling and raising any exceptions encountered
        raise e
