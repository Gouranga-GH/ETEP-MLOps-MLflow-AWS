import os  # Importing the os module for interacting with the operating system
from pathlib import Path  # Importing Path from the pathlib module to handle file paths in a platform-independent way
import logging  # Importing the logging module to provide a flexible framework for emitting log messages

# Configuring logging to display messages with a specific format including timestamp and the log level
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Defining the project name which will be used in various file paths
project_name = "ETEP_MLOps_MLflow_AWS"

# List of files to be created for the project, including various directories and files
list_of_files = [
    ".github/workflows/.gitkeep",  # A placeholder file to ensure the directory is tracked by git
    f"src/{project_name}/__init__.py",  # Package initialization file for the main project directory
    f"src/{project_name}/components/__init__.py",  # Package initialization file for the components module
    f"src/{project_name}/utils/__init__.py",  # Package initialization file for the utils module
    f"src/{project_name}/utils/common.py",  # A common utility module for shared functions
    f"src/{project_name}/config/__init__.py",  # Package initialization file for the config module
    f"src/{project_name}/config/configuration.py",  # Module for configuration management
    f"src/{project_name}/pipeline/__init__.py",  # Package initialization file for the pipeline module
    f"src/{project_name}/entity/__init__.py",  # Package initialization file for the entity module
    f"src/{project_name}/entity/config_entity.py",  # Module defining configuration entities
    f"src/{project_name}/constants/__init__.py",  # Package initialization file for the constants module
    "config/config.yaml",  # YAML file for storing configuration settings
    "params.yaml",  # YAML file for storing parameters # To be updated during model training
    "schema.yaml",  # YAML file for defining data schema # To be updated during model validation
    "main.py",  # Main entry point for the project
    "app.py",  # Application entry point (likely for a web app or service)
    "Dockerfile",  # Dockerfile for containerizing the application
    "requirements.txt",  # File listing Python dependencies
    "setup.py",  # Script for setting up the Python package
    "research/trials.ipynb",  # Jupyter notebook for research and experimentation
    "templates/index.html",  # HTML template for the web interface
    "test.py"  # Script for running tests
]

# Looping through each file path in the list_of_files
for filepath in list_of_files:
    filepath = Path(filepath)  # Converting the string file path to a Path object
    filedir, filename = os.path.split(filepath)  # Splitting the file path into directory and file name

    # If the directory part of the file path is not empty, create the directory
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Creating the directory if it doesn't exist, including intermediate directories
        logging.info(f"Creating directory: {filedir} for the file: {filename}")  # Logging the creation of the directory

    # If the file does not exist or is empty, create an empty file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:  # Opening the file in write mode to create it
            pass  # Pass statement, as we just want to create an empty file
        logging.info(f"Creating empty file: {filepath}")  # Logging the creation of the file

    # If the file already exists and is not empty, log that it already exists
    else:
        logging.info(f"{filename} already exists")  # Logging that the file already exists
