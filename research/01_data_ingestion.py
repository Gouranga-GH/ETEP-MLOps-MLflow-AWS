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

# Defining a frozen dataclass to hold configuration for data ingestion
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path  # Root directory for data ingestion
    source_URL: str  # URL from where data will be downloaded
    local_data_file: Path  # Path where the downloaded file will be stored
    unzip_dir: Path  # Directory where the data will be unzipped

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

    # Function to get data ingestion configuration settings
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        # Creating directories based on configuration
        create_directories([config.root_dir])

        # Initializing the DataIngestionConfig object with necessary paths and settings
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config

# Importing additional libraries for file downloading, extracting, and logging
import urllib.request as request  # For downloading files from URLs
import zipfile  # For handling zip files
from src.ETEP_MLOps_MLflow_AWS.utils import logger  # Custom logger utility
from src.ETEP_MLOps_MLflow_AWS.utils.common import get_size  # Function to get file size

# Data ingestion class to handle file downloading and extraction
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config  # Storing the configuration object

    # Function to download the file if it doesn't already exist
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            # Downloading the file from the specified URL
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded! with the following info: \n{headers}")
        else:
            # Logging if the file already exists and displaying its size
            logger.info(f"File already exists with size: {get_size(Path(self.config.local_data_file))}")

    # Function to extract the zip file
    def extract_zip_file(self):
        """
        Extracts the zip file into the specified directory.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)  # Creating the extraction directory if it doesn't exist
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)  # Extracting all files into the specified directory
        logger.info(f"Extraction completed successfully at {unzip_path}")

# Main execution block to run the data ingestion process
if __name__ == "__main__":
    try:
        # Initializing configuration manager and getting ingestion configuration
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()

        # Creating a DataIngestion object and running the file download and extraction
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
    except Exception as e:
        # Handling and raising any exceptions encountered
        raise e
