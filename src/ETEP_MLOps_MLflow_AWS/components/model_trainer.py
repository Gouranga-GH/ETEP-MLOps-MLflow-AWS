import pandas as pd  # For data manipulation
import os  # For interacting with the operating system, such as file operations
from src.ETEP_MLOps_MLflow_AWS.utils import logger  # Importing a logger utility
from sklearn.linear_model import ElasticNet  # Importing ElasticNet model
import joblib  # For saving the trained model
from src.ETEP_MLOps_MLflow_AWS.entity.config_entity import ModelTrainerConfig  # Importing ModelTrainerConfig class

# Definition of the ModelTrainer class
class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        # Initializing the class with a ModelTrainerConfig object
        self.config = config

    # Method to train the ElasticNet model
    def train(self):
        # Load training and test data from CSV files
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        # Separate features and target variable from training and test data
        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]

        # Initialize and train the ElasticNet model
        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
        lr.fit(train_x, train_y)

        # Save the trained model to a file
        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))
