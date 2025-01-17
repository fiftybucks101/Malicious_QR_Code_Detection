from MaliciousQRCodeDetection.logging.logger import logger
from MaliciousQRCodeDetection.exception import MaliciousQRException
from MaliciousQRCodeDetection.entity.config_entity import ModelTrainerConfig
from MaliciousQRCodeDetection.config.configuration import ConfigurationManager
from MaliciousQRCodeDetection.components.model_training import ModelTrainer
import sys

STAGE_NAME = "Model Training Stage"

class ModelTrainerTrainingPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(model_trainer_config)
        model_trainer.Train()

if __name__ == '__main__':
    try:
        logger.info(f">>>>> Stage: {STAGE_NAME} started <<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        raise MaliciousQRException(e,sys)