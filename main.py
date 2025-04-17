from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline
from src.datascience.pipeline.model_evaluation_pipeline import ModelEvaluationTrainingPipeline


# Stage 1: Data Ingestion
STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    ingestion_pipeline = DataIngestionTrainingPipeline()
    ingestion_pipeline.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

# Stage 2: Data Validation
STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    validation_pipeline = DataValidationTrainingPipeline()
    validation_pipeline.initiate_data_validation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

# Stage 3: Data Transformation
STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    transformation_pipeline = DataTransformationTrainingPipeline()
    transformation_pipeline.initiate_data_transformation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

# Stage 4: Model Training
STAGE_NAME = "Model Trainer stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    trainer_pipeline = ModelTrainerTrainingPipeline()
    trainer_pipeline.initiate_model_training()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

# Stage 5: Model Evaluation
STAGE_NAME = "Model Evaluation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    evaluation_pipeline = ModelEvaluationTrainingPipeline()
    evaluation_pipeline.initiate_model_evaluation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
