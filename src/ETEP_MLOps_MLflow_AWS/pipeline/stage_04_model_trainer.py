from src.ETEP_MLOps_MLflow_AWS.config.configuration import ConfigurationManager  # Importing ConfigurationManager class
from src.ETEP_MLOps_MLflow_AWS.components.model_trainer import ModelTrainer  # Importing ModelTrainer class
from src.ETEP_MLOps_MLflow_AWS.utils import logger  # Importing a logger utility

# Define the stage name for logging purposes
STAGE_NAME = "Model Trainer stage"

# Definition of the ModelTrainerTrainingPipeline class
class ModelTrainerTrainingPipeline:
    def __init__(self):
        # Initialize the pipeline object (no specific initialization here)
        pass

    # Main method to execute the model training process
    def main(self):
        # Create a ConfigurationManager instance to access configuration settings
        config = ConfigurationManager()
        
        # Get model trainer configuration from the ConfigurationManager
        model_trainer_config = config.get_model_trainer_config()
        
        # Create a ModelTrainer instance with the configuration
        model_trainer = ModelTrainer(config=model_trainer_config)
        
        # Execute the training method for the model
        model_trainer.train()

# Main entry point of the script
if __name__ == '__main__':
    try:
        # Log the start of the model training stage
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        
        # Create an instance of ModelTrainerTrainingPipeline
        obj = ModelTrainerTrainingPipeline()
        
        # Execute the main method of the pipeline
        obj.main()
        
        # Log the completion of the model training stage
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        # Log any exceptions that occur and re-raise them
        logger.exception(e)
        raise e
