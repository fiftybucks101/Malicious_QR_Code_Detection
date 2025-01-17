from MaliciousQRCodeDetection.logging.logger import logger
from MaliciousQRCodeDetection.exception import MaliciousQRException
from MaliciousQRCodeDetection.entity.config_entity import ModelEvaluationConfig
from MaliciousQRCodeDetection.config.configuration import ConfigurationManager
from MaliciousQRCodeDetection.components.model_evaluation import ModelEvaluation
import sys

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(model_evaluation_config)
        model_evaluation.metrics()

if __name__ == '__main__':
    try:
        logger.info(f">>>>> Stage: {STAGE_NAME} started <<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        raise MaliciousQRException(e,sys)