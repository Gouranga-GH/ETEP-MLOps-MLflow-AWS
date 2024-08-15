import os  # For interacting with the operating system, such as file operations
from src.ETEP_MLOps_MLflow_AWS.utils import logger  # Importing a logger utility
from src.ETEP_MLOps_MLflow_AWS.entity.config_entity import DataValidationConfig  # Importing DataValidationConfig class
import pandas as pd  # Importing pandas for data manipulation

# Definition of the DataValidation class
class DataValidation:
    def __init__(self, config: DataValidationConfig):
        # Initializing the class with a DataValidationConfig object
        self.config = config

    # Method to validate that all columns in the data match the schema
    def validate_all_columns(self) -> bool:
        try:
            # Initialize validation status
            validation_status = None

            # Load the dataset from the path specified in the configuration
            data = pd.read_csv(self.config.unzip_data_dir)
            # Get the list of columns in the dataset
            all_cols = list(data.columns)

            # Get the expected columns from the schema
            all_schema = self.config.all_schema.keys()

            # Validate each column in the dataset against the schema
            for col in all_cols:
                if col not in all_schema:
                    # If a column is not in the schema, set validation status to False
                    validation_status = False
                    # Write the validation status to the status file
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    # If a column is in the schema, set validation status to True
                    validation_status = True
                    # Write the validation status to the status file
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            # Return the final validation status
            return validation_status

        except Exception as e:
            # Log and raise any exceptions that occur
            logger.error(f"Error during validation: {e}")
            raise e
