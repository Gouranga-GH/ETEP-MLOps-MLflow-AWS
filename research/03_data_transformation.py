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

# Defining a frozen dataclass to hold configuration for data transformation
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path  # Root directory for storing transformed data
    data_path: Path  # Path of the raw data file to be transformed

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

    # Function to get data transformation configuration settings
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        # Creating directories based on configuration
        create_directories([config.root_dir])

        # Initializing the DataTransformationConfig object with necessary paths and settings
        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
        )

        return data_transformation_config

# Importing additional libraries for data processing, logging, and splitting the data
from src.ETEP_MLOps_MLflow_AWS.utils import logger  # Custom logger utility
from sklearn.model_selection import train_test_split  # For splitting the data
import pandas as pd  # For data manipulation and analysis

# Data transformation class to handle data splitting and preprocessing
class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config  # Storing the configuration object

    # Function to split the data into training and test sets
    def train_test_spliting(self):
        # Reading the data from the specified path
        data = pd.read_csv(self.config.data_path)

        # Splitting the data into training and test sets (default split is 0.75, 0.25)
        train, test = train_test_split(data)

        # Saving the training and test sets as CSV files
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        # Logging information about the split
        logger.info("Split data into training and test sets")
        logger.info(f"Training set shape: {train.shape}")
        logger.info(f"Test set shape: {test.shape}")

        # Printing the shapes of the split datasets
        print(train.shape)
        print(test.shape)

# Main execution block to run the data transformation process
if __name__ == "__main__":
    try:
        # Initializing configuration manager and getting transformation configuration
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()

        # Creating a DataTransformation object and running the data splitting
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.train_test_spliting()
    except Exception as e:
        # Handling and raising any exceptions encountered
        raise e
