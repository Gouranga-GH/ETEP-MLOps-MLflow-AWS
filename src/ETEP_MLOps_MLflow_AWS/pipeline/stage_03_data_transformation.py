from src.ETEP_MLOps_MLflow_AWS.config.configuration import ConfigurationManager  # Importing ConfigurationManager class
from src.ETEP_MLOps_MLflow_AWS.components.data_transformation import DataTransformation  # Importing DataTransformation class
from src.ETEP_MLOps_MLflow_AWS.utils import logger  # Importing a logger utility
from pathlib import Path  # For handling file paths

# Define the stage name for logging purposes
STAGE_NAME = "Data Transformation stage"

# Definition of the DataTransformationTrainingPipeline class
class DataTransformationTrainingPipeline:
    def __init__(self):
        # Initialize the pipeline object (no specific initialization here)
        pass

    # Main method to execute the data transformation process
    def main(self):
        try:
            # Read the status of the data validation from a file
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            # Proceed with data transformation if the validation status is "True"
            if status == "True":
                # Create a ConfigurationManager instance to access configuration settings
                config = ConfigurationManager()
                
                # Get data transformation configuration from the ConfigurationManager
                data_transformation_config = config.get_data_transformation_config()
                
                # Create a DataTransformation instance with the configuration
                data_transformation = DataTransformation(config=data_transformation_config)
                
                # Execute the data transformation method to split the data
                data_transformation.train_test_spliting()
            else:
                # Raise an exception if the data validation status is not "True"
                raise Exception("Your data schema is not valid")

        except Exception as e:
            # Print any exceptions that occur
            print(e)

# Main entry point of the script
if __name__ == '__main__':
    try:
        # Log the start of the data transformation stage
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        
        # Create an instance of DataTransformationTrainingPipeline
        obj = DataTransformationTrainingPipeline()
        
        # Execute the main method of the pipeline
        obj.main()
        
        # Log the completion of the data transformation stage
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        # Log any exceptions that occur and re-raise them
        logger.exception(e)
        raise e
