import os
import pandas as pd
import sys
from MaliciousQRCodeDetection.logging.logger import logger
from MaliciousQRCodeDetection.exception import MaliciousQRException
from  MaliciousQRCodeDetection.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self,config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status: None

            train_data = pd.read_csv(self.config.train_data)
            test_data = pd.read_csv(self.config.test_data)

            combined_data = pd.concat([train_data, test_data], axis=0, ignore_index=True)

            all_cols = list(combined_data.columns)
            all_schema = list(self.config.schema['columns'].keys())

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.status_file, 'w') as f:
                        f.write(f"Validation Status: {validation_status}")
            else:
                validation_status = True
                with open(self.config.status_file, 'w') as f:
                    f.write(f"Validation Status: {validation_status}")
            logger.info('Data validation successfully done..')
            return validation_status            
        except Exception as e:
            raise MaliciousQRException(e,sys)