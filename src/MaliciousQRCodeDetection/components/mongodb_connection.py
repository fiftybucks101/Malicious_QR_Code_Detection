import os
import pymongo
import certifi
import pandas as pd
import numpy as np
from dotenv import load_dotenv
from MaliciousQRCodeDetection.exception import MaliciousQRException
from MaliciousQRCodeDetection.logging.logger import logger
from MaliciousQRCodeDetection.constants import db_name, mongodb_url_key, collection_name
import sys

class MongoDBClient:
    """
    MongoDBClient: Handles MongoDB connection and data export.

    Methods:
    - __init__: Initializes MongoDB client connection.
    - export_collection_as_dataframe: Exports a MongoDB collection to a Pandas DataFrame.
    """
    def __init__(self, database_name=db_name, collection_name=collection_name) -> None:
        try:
            # Load environment variables
            load_dotenv('project.env')
            mongo_db_url = os.getenv(mongodb_url_key)
            if not mongo_db_url:
                raise ValueError(f"Environment variable '{mongodb_url_key}' is not set.")
            
            # Create MongoDB client
            self.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=certifi.where())
            self.database = self.client[database_name]
            self.collection_name = collection_name
            logger.info("MongoDB connection established successfully.")
        except Exception as e:
            raise MaliciousQRException(e,sys)

    def export_collection_as_dataframe(self) -> pd.DataFrame:
        """
        Exports the specified collection as a Pandas DataFrame.
        
        Returns:
            pd.DataFrame: The MongoDB collection as a DataFrame.
        """
        try:
            collection = self.database[self.collection_name]
            data = list(collection.find())
            
            # Convert to DataFrame and clean up
            df = pd.DataFrame(data)
            if "_id" in df.columns:
                df.drop(columns=["_id"], inplace=True)
            df.replace({"na": np.nan}, inplace=True)
            return df
        except Exception as e:
            raise MaliciousQRException(e,sys)
