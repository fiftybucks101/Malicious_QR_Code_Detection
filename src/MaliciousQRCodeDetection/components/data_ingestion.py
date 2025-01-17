from MaliciousQRCodeDetection.entity.config_entity import DataIngestionConfig
import urllib.request as request
from MaliciousQRCodeDetection.utils.common import get_size
from MaliciousQRCodeDetection.logging.logger import logger
from pathlib import Path
import os
import pandas as pd
from MaliciousQRCodeDetection.exception import MaliciousQRException
import sys

class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        try:
            if not os.path.exists(self.config.csv_file):
                filename, headers = request.urlretrieve(
                    url = self.config.source_URL,
                    filename=self.config.csv_file
                )
                logger.info(f"{filename} downloaded! with following info: \n{headers}")
            else:
                logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
        except Exception as e:
            logger.error(f"Failed to download file: {str(e)}")

    # def load_csv_from_local_source(self):
    #     try:
    #         # Check if the source file exists
    #         if os.path.exists(self.config.source_URL):
    #             # Load the CSV file using pandas
    #             df = pd.read_csv(self.config.source_URL)
    #             logger.info(f"CSV file loaded successfully from {self.config.source_URL}.")
    #             # Save the loaded CSV to the target location
    #             os.makedirs(os.path.dirname(self.config.csv_dir), exist_ok=True)
    #             df.to_csv(self.config.csv_file, index=False)
    #             logger.info(f"CSV file saved to {self.config.csv_file}.")
    #         else:
    #             logger.error(f"Source file does not exist: {self.config.source_URL}")
    #             raise FileNotFoundError(f"Source file not found: {self.config.source_URL}")
    #     except Exception as e:
    #         logger.info(f"Failed to load or save CSV file: {str(e)}")
    #         raise MaliciousQRException(e,sys)
            