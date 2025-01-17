from MaliciousQRCodeDetection.logging.logger import logger
from MaliciousQRCodeDetection.exception import MaliciousQRException
from MaliciousQRCodeDetection.entity.config_entity import DataValidationConfig
from MaliciousQRCodeDetection.config.configuration import ConfigurationManager
from MaliciousQRCodeDetection.components.data_validation import DataValidation
import sys

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.validate_all_columns()


if __name__ == '__main__':
    try:
        logger.info(f">>>>> Stage: {STAGE_NAME} started <<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        raise MaliciousQRException(e,sys)