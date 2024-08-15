# Importing necessary libraries
import os  # For changing directory paths
import pandas as pd  # For data manipulation and analysis

# Checking the current working directory
print(os.getcwd())

# Changing the directory to one level up
os.chdir("../")

# Checking the new current working directory
print(os.getcwd())

# Loading the dataset
data = pd.read_csv("artifacts/data_ingestion/winequality-red.csv")

# Displaying the first few rows of the dataset
print(data.head())

# Displaying dataset information (e.g., data types, memory usage)
data.info()

# Checking for any missing values in the dataset
print(data.isnull().sum())

# Displaying the shape of the dataset (rows, columns)
print(data.shape)

# Displaying the column names in the dataset
print(data.columns)

# Importing additional necessary libraries and modules
from dataclasses import dataclass  # For creating configuration classes
from pathlib import Path  # For managing file paths

# Defining a frozen dataclass to hold configuration for data validation
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path  # Root directory path
    STATUS_FILE: str  # Path for storing status of validation
    unzip_data_dir: Path  # Directory path of unzipped data
    all_schema: dict  # Dictionary holding the schema information

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

    # Function to get data validation configuration settings
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        # Creating directories based on configuration
        create_directories([config.root_dir])

        # Initializing the DataValidationConfig object with necessary paths and schema
        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir=config.unzip_data_dir,
            all_schema=schema,
        )

        return data_validation_config

# Importing logger utility and pandas for data validation
from src.ETEP_MLOps_MLflow_AWS.utils import logger

# Data validation class to handle column validation
class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config  # Storing the configuration object

    # Function to validate all columns in the dataset
    def validate_all_columns(self) -> bool:
        try:
            validation_status = None  # Placeholder for validation status

            # Reading the CSV file from the configured directory
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)  # Getting all columns from the dataset

            all_schema = self.config.all_schema.keys()  # Extracting expected columns from the schema

            # Validating if all expected columns exist in the dataset
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    # Writing validation status to a status file
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    # Writing validation status to a status file
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            raise e  # Raising any exceptions encountered

# Main execution block to run the validation
if __name__ == "__main__":
    try:
        # Initializing configuration manager and getting validation configuration
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()

        # Creating a DataValiadtion object and running the validation
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_columns()
    except Exception as e:
        raise e  # Raising any exceptions encountered
