from src.ETEP_MLOps_MLflow_AWS.utils import logger  # Importing logger utility for logging
from src.ETEP_MLOps_MLflow_AWS.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline  # Importing Data Ingestion pipeline class
from src.ETEP_MLOps_MLflow_AWS.pipeline.stage_02_data_validation import DataValidationTrainingPipeline  # Importing Data Validation pipeline class
from src.ETEP_MLOps_MLflow_AWS.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline  # Importing Data Transformation pipeline class
from src.ETEP_MLOps_MLflow_AWS.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline  # Importing Model Trainer pipeline class
from src.ETEP_MLOps_MLflow_AWS.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline  # Importing Model Evaluation pipeline class

# Data Ingestion Stage
STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")  # Log the start of the Data Ingestion stage
    data_ingestion = DataIngestionTrainingPipeline()  # Initialize Data Ingestion pipeline
    data_ingestion.main()  # Execute the main method of Data Ingestion pipeline
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")  # Log the completion of the Data Ingestion stage
except Exception as e:
    logger.exception(e)  # Log any exception that occurs
    raise e  # Re-raise the exception

# Data Validation Stage
STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")  # Log the start of the Data Validation stage
    data_validation = DataValidationTrainingPipeline()  # Initialize Data Validation pipeline
    data_validation.main()  # Execute the main method of Data Validation pipeline
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")  # Log the completion of the Data Validation stage
except Exception as e:
    logger.exception(e)  # Log any exception that occurs
    raise e  # Re-raise the exception

# Data Transformation Stage
STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")  # Log the start of the Data Transformation stage
    data_transformation = DataTransformationTrainingPipeline()  # Initialize Data Transformation pipeline
    data_transformation.main()  # Execute the main method of Data Transformation pipeline
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")  # Log the completion of the Data Transformation stage
except Exception as e:
    logger.exception(e)  # Log any exception that occurs
    raise e  # Re-raise the exception

# Model Trainer Stage
STAGE_NAME = "Model Trainer stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")  # Log the start of the Model Trainer stage
    model_trainer = ModelTrainerTrainingPipeline()  # Initialize Model Trainer pipeline
    model_trainer.main()  # Execute the main method of Model Trainer pipeline
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")  # Log the completion of the Model Trainer stage
except Exception as e:
    logger.exception(e)  # Log any exception that occurs
    raise e  # Re-raise the exception

# Model Evaluation Stage
STAGE_NAME = "Model evaluation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")  # Log the start of the Model Evaluation stage
    model_evaluation = ModelEvaluationTrainingPipeline()  # Initialize Model Evaluation pipeline
    model_evaluation.main()  # Execute the main method of Model Evaluation pipeline
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")  # Log the completion of the Model Evaluation stage
except Exception as e:
    logger.exception(e)  # Log any exception that occurs
    raise e  # Re-raise the exception
