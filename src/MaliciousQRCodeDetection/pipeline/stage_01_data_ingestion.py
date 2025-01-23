from MaliciousQRCodeDetection.entity.config_entity import DataIngestionConfig
from MaliciousQRCodeDetection.config.configuration import ConfigurationManager
from MaliciousQRCodeDetection.logging.logger import logger
from MaliciousQRCodeDetection.components.data_ingestion import DataIngestion
from MaliciousQRCodeDetection.exception import MaliciousQRException
import sys


STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def stage_01(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.export_data_into_data_store() 


if __name__ == '__main__':
    try:
        logger.info(f">>>>> Stage: {STAGE_NAME} started <<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.stage_01()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        raise MaliciousQRException(e,sys)