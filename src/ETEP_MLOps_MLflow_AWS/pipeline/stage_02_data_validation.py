from src.ETEP_MLOps_MLflow_AWS.config.configuration import ConfigurationManager  # Importing ConfigurationManager class
from src.ETEP_MLOps_MLflow_AWS.components.data_validation import DataValidation
  # Importing DataValidation class 
from src.ETEP_MLOps_MLflow_AWS.utils import logger  # Importing a logger utility

# Define the stage name for logging purposes
STAGE_NAME = "Data Validation stage"

# Definition of the DataValidationTrainingPipeline class
class DataValidationTrainingPipeline:
    def __init__(self):
        # Initialize the pipeline object (no specific initialization here)
        pass

    # Main method to execute the data validation process
    def main(self):
        # Create a ConfigurationManager instance to access configuration settings
        config = ConfigurationManager()
        
        # Get data validation configuration from the ConfigurationManager
        data_validation_config = config.get_data_validation_config()
        
        # Create a DataValiadtion instance with the configuration
        # Note: The class name should be corrected to DataValidation if there was a typo
        data_validation = DataValidation(config=data_validation_config)
        
        # Execute the data validation method to check column consistency
        data_validation.validate_all_columns()

# Main entry point of the script
if __name__ == '__main__':
    try:
        # Log the start of the data validation stage
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        
        # Create an instance of DataValidationTrainingPipeline
        obj = DataValidationTrainingPipeline()
        
        # Execute the main method of the pipeline
        obj.main()
        
        # Log the completion of the data validation stage
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        # Log any exceptions that occur and re-raise them
        logger.exception(e)
        raise e
