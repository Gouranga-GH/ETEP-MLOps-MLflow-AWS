import os  # For interacting with the operating system, such as file operations
import urllib.request as request  # For downloading files from the web
import zipfile  # For handling zip file extraction
from src.ETEP_MLOps_MLflow_AWS.utils import logger  # Importing a logger utility
from src.ETEP_MLOps_MLflow_AWS.utils.common import get_size  # Importing a utility to get file size
from pathlib import Path  # For handling file system paths
from src.ETEP_MLOps_MLflow_AWS.entity.config_entity import DataIngestionConfig  # Importing DataIngestionConfig class

# Definition of the DataIngestion class
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        # Initializing the class with a DataIngestionConfig object
        self.config = config

    def download_file(self):
        # Check if the file does not already exist
        if not os.path.exists(self.config.local_data_file):
            # Download the file from the URL specified in the configuration
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            # Log the successful download with filename and headers
            logger.info(f"{filename} downloaded! with following info: \n{headers}")
        else:
            # If the file already exists, log its size
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """
        Extracts the zip file into the specified directory.
        The function does not return anything.
        """
        # Path where the zip file will be extracted
        unzip_path = self.config.unzip_dir
        # Create the directory if it doesn't exist
        os.makedirs(unzip_path, exist_ok=True)
        # Open the zip file and extract its contents
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
