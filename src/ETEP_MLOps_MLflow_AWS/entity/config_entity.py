# Importing the necessary modules
from dataclasses import dataclass  # For creating data classes
from pathlib import Path  # For handling file system paths

# Defining a data class for configuration related to data ingestion
@dataclass(frozen=True)
class DataIngestionConfig:
    # The root directory for the project
    root_dir: Path
    # URL from which the data will be sourced
    source_URL: str
    # Path to the local file where the data will be stored
    local_data_file: Path
    # Directory where the data will be unzipped
    unzip_dir: Path

# Defining a data class for configuration related to data validation
@dataclass(frozen=True)
class DataValidationConfig:
    # The root directory for the project
    root_dir: Path
    # Name of the status file for validation
    STATUS_FILE: str
    # Directory where the unzipped data is located
    unzip_data_dir: Path
    # Schema to be used for validation, represented as a dictionary
    all_schema: dict

# Defining a data class for configuration related to data transformation
@dataclass(frozen=True)
class DataTransformationConfig:
    # The root directory for the project
    root_dir: Path
    # Path to the data that needs to be transformed
    data_path: Path

# Defining a data class for configuration related to model training
@dataclass(frozen=True)
class ModelTrainerConfig:
    # The root directory for the project
    root_dir: Path
    # Path to the training data
    train_data_path: Path
    # Path to the testing data
    test_data_path: Path
    # Name of the model to be trained
    model_name: str
    # Regularization parameter for the model
    alpha: float
    # Ratio of L1 regularization to L2 regularization
    l1_ratio: float
    # Name of the target column in the dataset
    target_column: str

# Defining a data class for configuration related to model evaluation
@dataclass(frozen=True)
class ModelEvaluationConfig:
    # The root directory for the project
    root_dir: Path
    # Path to the testing data
    test_data_path: Path
    # Path to the model that will be evaluated
    model_path: Path
    # Parameters to be used for evaluation, represented as a dictionary
    all_params: dict
    # File name where evaluation metrics will be saved
    metric_file_name: Path
    # Name of the target column in the dataset
    target_column: str
    # URI for MLflow, a tool for managing machine learning experiments
    mlflow_uri: str
