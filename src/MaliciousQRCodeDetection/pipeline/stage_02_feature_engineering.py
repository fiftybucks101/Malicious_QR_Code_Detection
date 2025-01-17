from MaliciousQRCodeDetection.logging.logger import logger
from MaliciousQRCodeDetection.exception import MaliciousQRException
from MaliciousQRCodeDetection.entity.config_entity import FeatureEngineeringConfig
from MaliciousQRCodeDetection.config.configuration import ConfigurationManager
from MaliciousQRCodeDetection.components.feature_engineering import FeatureEngineering

import sys

STAGE_NAME = "Feature Engineering Stage"

class FeatureEngineeringTrainingPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        feature_engineering_config = config.get_feature_engineering_config()
        feature_engineering = FeatureEngineering(config=feature_engineering_config)
        feature_engineering.train_test_split()


if __name__ == '__main__':
    try:
        logger.info(f">>>>> Stage: {STAGE_NAME} started <<<<<")
        obj = FeatureEngineeringTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        raise MaliciousQRException(e,sys)