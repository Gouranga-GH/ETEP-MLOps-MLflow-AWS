# Importing necessary modules and functions
from src.ETEP_MLOps_MLflow_AWS.constants import *  # Importing constants from the constants module
from src.ETEP_MLOps_MLflow_AWS.utils.common import read_yaml, create_directories  # Importing utility functions for reading YAML files and creating directories
from src.ETEP_MLOps_MLflow_AWS.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
    ModelEvaluationConfig
)  # Importing data classes for different configurations

# Definition of the ConfigurationManager class
class ConfigurationManager:
    # Initializer method for the ConfigurationManager class
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,  # Path to the configuration file
        params_filepath=PARAMS_FILE_PATH,  # Path to the parameters file
        schema_filepath=SCHEMA_FILE_PATH  # Path to the schema file
    ):
        # Reading configuration, parameters, and schema from YAML files
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        # Creating directories specified in the configuration
        create_directories([self.config.artifacts_root])

    # Method to get data ingestion configuration
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        # Accessing data ingestion configuration from the read YAML
        config = self.config.data_ingestion

        # Creating necessary directories for data ingestion
        create_directories([config.root_dir])

        # Creating and returning a DataIngestionConfig object
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config

    # Method to get data validation configuration
    def get_data_validation_config(self) -> DataValidationConfig:
        # Accessing data validation configuration and schema from the read YAML
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        # Creating necessary directories for data validation
        create_directories([config.root_dir])

        # Creating and returning a DataValidationConfig object
        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir=config.unzip_data_dir,
            all_schema=schema,
        )

        return data_validation_config

    # Method to get data transformation configuration
    def get_data_transformation_config(self) -> DataTransformationConfig:
        # Accessing data transformation configuration from the read YAML
        config = self.config.data_transformation

        # Creating necessary directories for data transformation
        create_directories([config.root_dir])

        # Creating and returning a DataTransformationConfig object
        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
        )

        return data_transformation_config

    # Method to get model trainer configuration
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        # Accessing model trainer configuration, parameters, and schema from the read YAML
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN

        # Creating necessary directories for model training
        create_directories([config.root_dir])

        # Creating and returning a ModelTrainerConfig object
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

    # Method to get model evaluation configuration
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        # Accessing model evaluation configuration, parameters, and schema from the read YAML
        config = self.config.model_evaluation
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN

        # Creating necessary directories for model evaluation
        create_directories([config.root_dir])

        # Creating and returning a ModelEvaluationConfig object
        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path=config.model_path,
            all_params=params,
            metric_file_name=config.metric_file_name,
            target_column=schema.name,
            mlflow_uri="https://dagshub.com/Gouranga-GH/ETEP-MLOps-MLflow-AWS.mlflow"  # URI for MLflow
        )

        return model_evaluation_config
