from src.ETEP_MLOps_MLflow_AWS.config.configuration import ConfigurationManager  # Importing ConfigurationManager class
from src.ETEP_MLOps_MLflow_AWS.components.data_ingestion import DataIngestion  # Importing DataIngestion class
from src.ETEP_MLOps_MLflow_AWS.utils import logger  # Importing a logger utility

# Define the stage name for logging purposes
STAGE_NAME = "Data Ingestion stage"

# Definition of the DataIngestionTrainingPipeline class
class DataIngestionTrainingPipeline:
    def __init__(self):
        # Initialize the pipeline object (no specific initialization here)
        pass

    # Main method to execute the data ingestion process
    def main(self):
        # Create a ConfigurationManager instance to access configuration settings
        config = ConfigurationManager()
        
        # Get data ingestion configuration from the ConfigurationManager
        data_ingestion_config = config.get_data_ingestion_config()
        
        # Create a DataIngestion instance with the configuration
        data_ingestion = DataIngestion(config=data_ingestion_config)
        
        # Download the data file from the specified URL
        data_ingestion.download_file()
        
        # Extract the downloaded zip file to the specified directory
        data_ingestion.extract_zip_file()

# Main entry point of the script
if __name__ == '__main__':
    try:
        # Log the start of the data ingestion stage
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        
        # Create an instance of DataIngestionTrainingPipeline
        obj = DataIngestionTrainingPipeline()
        
        # Execute the main method of the pipeline
        obj.main()
        
        # Log the completion of the data ingestion stage
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        # Log any exceptions that occur and re-raise them
        logger.exception(e)
        raise e
