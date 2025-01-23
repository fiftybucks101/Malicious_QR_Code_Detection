from MaliciousQRCodeDetection.entity.config_entity import DataIngestionConfig
import urllib.request as request
from MaliciousQRCodeDetection.utils.common import get_size
from MaliciousQRCodeDetection.logging.logger import logger
from pathlib import Path
import os
import pandas as pd
from MaliciousQRCodeDetection.exception import MaliciousQRException
import sys
from MaliciousQRCodeDetection.components.mongodb_connection import MongoDBClient


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        '''
        param data_ingestion_config: configuration for data ingestion
        '''

        try:
            self.config = config
        except Exception as e:
            raise MaliciousQRException(e,sys)

    def export_data_into_data_store(self):
        try:
            data = MongoDBClient()
            df = data.export_collection_as_dataframe()

            if not os.path.exists(self.config.csv_file):
                df.to_csv(self.config.csv_file,index=False)
                logger.info('Csv file successully saved in artifacts data ingestion')
            else:
                logger.info('CSV file already exists in artifacts data ingestion')

        except Exception as e:
            raise MaliciousQRException(e,sys)