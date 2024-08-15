from src.ETEP_MLOps_MLflow_AWS.config.configuration import ConfigurationManager  # Importing ConfigurationManager class
from src.ETEP_MLOps_MLflow_AWS.components.model_evaluation import ModelEvaluation  # Importing ModelEvaluation class
from src.ETEP_MLOps_MLflow_AWS.utils import logger  # Importing a logger utility

# Define the stage name for logging purposes
STAGE_NAME = "Model evaluation stage"

# Definition of the ModelEvaluationTrainingPipeline class
class ModelEvaluationTrainingPipeline:
    def __init__(self):
        # Initialize the pipeline object (no specific initialization here)
        pass

    # Main method to execute the model evaluation process
    def main(self):
        # Create a ConfigurationManager instance to access configuration settings
        config = ConfigurationManager()
        
        # Get model evaluation configuration from the ConfigurationManager
        model_evaluation_config = config.get_model_evaluation_config()
        
        # Create a ModelEvaluation instance with the configuration
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        
        # Execute the evaluation method for logging results into MLflow
        model_evaluation.log_into_mlflow()

# Main entry point of the script
if __name__ == '__main__':
    try:
        # Log the start of the model evaluation stage
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        
        # Create an instance of ModelEvaluationTrainingPipeline
        obj = ModelEvaluationTrainingPipeline()
        
        # Execute the main method of the pipeline
        obj.main()
        
        # Log the completion of the model evaluation stage
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        # Log any exceptions that occur and re-raise them
        logger.exception(e)
        raise e
