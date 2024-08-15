# Importing necessary libraries
import os  # For directory operations
from dataclasses import dataclass  # For creating configuration classes
from pathlib import Path  # For handling file paths

# Displaying the current working directory
print(os.getcwd())

# Changing the directory to one level up
os.chdir("../")

# Displaying the new current working directory
print(os.getcwd())

# Defining a frozen dataclass to hold configuration for model training
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path  # Root directory for storing model artifacts
    train_data_path: Path  # Path to the training data
    test_data_path: Path  # Path to the test data
    model_name: str  # Name of the model file to be saved
    alpha: float  # Alpha parameter for ElasticNet
    l1_ratio: float  # L1 ratio parameter for ElasticNet
    target_column: str  # Name of the target column in the dataset

# Importing custom constants and utility functions
from src.ETEP_MLOps_MLflow_AWS.constants import *
from src.ETEP_MLOps_MLflow_AWS.utils.common import read_yaml, create_directories

# Configuration manager class to handle reading configurations and setting up directories
class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH, schema_filepath=SCHEMA_FILE_PATH):
        # Reading configurations from YAML files
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        # Creating necessary directories for artifacts
        create_directories([self.config.artifacts_root])

    # Function to get model trainer configuration settings
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN

        # Creating directories based on configuration
        create_directories([config.root_dir])

        # Initializing the ModelTrainerConfig object with necessary paths and settings
        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            model_name=config.model_name,
            alpha=params.alpha,
            l1_ratio=params.l1_ratio,
            target_column=schema.name
        )

        return model_trainer_config

# Importing additional libraries for model training and serialization
import pandas as pd  # For data manipulation and analysis
from sklearn.linear_model import ElasticNet  # For building the regression model
import joblib  # For saving the trained model
from src.ETEP_MLOps_MLflow_AWS.utils import logger  # Custom logger utility

# Model trainer class to handle training the model and saving it
class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config  # Storing the configuration object

    # Function to train the model
    def train(self):
        # Reading the training and test data from CSV files
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        # Splitting the data into features (X) and target (y)
        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]

        # Initializing and training the ElasticNet model
        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
        lr.fit(train_x, train_y)

        # Saving the trained model using joblib
        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))
        logger.info(f"Model trained and saved as {self.config.model_name}")

# Main execution block to run the model training process
if __name__ == "__main__":
    try:
        # Initializing configuration manager and getting model trainer configuration
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()

        # Creating a ModelTrainer object and running the training process
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()
    except Exception as e:
        # Handling and raising any exceptions encountered
        raise e
