import os  # Importing the os module for interacting with the operating system
from box.exceptions import BoxValueError  # Importing BoxValueError for handling specific exceptions related to ConfigBox
import yaml  # Importing the yaml module for working with YAML files
from ETEP_MLOps_MLflow_AWS.utils import logger  # Importing the custom logger from package
import json  # Importing the json module for working with JSON data
import joblib  # Importing joblib for saving and loading binary files
from ensure import ensure_annotations  # Importing ensure_annotations to enforce function annotations at runtime
from box import ConfigBox  # Importing ConfigBox for enhanced dictionary handling with dot notation access
from pathlib import Path  # Importing Path from pathlib for platform-independent file paths
from typing import Any  # Importing Any for type hinting when the type can be anything

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its content as a ConfigBox.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        e: If any other exception occurs.

    Returns:
        ConfigBox: The contents of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml) as yaml_file:  # Opening the YAML file
            content = yaml.safe_load(yaml_file)  # Loading the YAML content
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")  # Logging successful load
            return ConfigBox(content)  # Returning content as ConfigBox for dot notation access
    except BoxValueError:
        raise ValueError("yaml file is empty")  # Raising error if the YAML file is empty
    except Exception as e:
        raise e  # Re-raising any other exception

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates a list of directories.

    Args:
        path_to_directories (list): List of directory paths to be created.
        verbose (bool, optional): Whether to log the creation of each directory. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)  # Creating the directory if it doesn't exist
        if verbose:
            logger.info(f"created directory at: {path}")  # Logging the creation of the directory

@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves data to a JSON file.

    Args:
        path (Path): Path to the JSON file.
        data (dict): Data to be saved in the JSON file.
    """
    with open(path, "w") as f:  # Opening the file in write mode
        json.dump(data, f, indent=4)  # Dumping the data into the file with indentation

    logger.info(f"json file saved at: {path}")  # Logging that the JSON file was saved

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads data from a JSON file.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: The loaded data as a ConfigBox for dot notation access.
    """
    with open(path) as f:  # Opening the file in read mode
        content = json.load(f)  # Loading the content from the JSON file

    logger.info(f"json file loaded successfully from: {path}")  # Logging that the JSON file was loaded
    return ConfigBox(content)  # Returning content as ConfigBox for dot notation access

@ensure_annotations
def save_bin(data: Any, path: Path):
    """Saves data to a binary file using joblib.

    Args:
        data (Any): The data to be saved as a binary file.
        path (Path): Path to the binary file.
    """
    joblib.dump(value=data, filename=path)  # Saving the data to the binary file using joblib
    logger.info(f"binary file saved at: {path}")  # Logging that the binary file was saved

@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads binary data using joblib.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: The object stored in the file.
    """
    data = joblib.load(path)  # Loading the binary data from the file
    logger.info(f"binary file loaded from: {path}")  # Logging that the binary file was loaded
    return data  # Returning the loaded data

@ensure_annotations
def get_size(path: Path) -> str:
    """Gets the size of a file in KB.

    Args:
        path (Path): Path to the file.

    Returns:
        str: The size of the file in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)  # Calculating the file size in KB
    return f"~ {size_in_kb} KB"  # Returning the size as a string with "KB" suffix
