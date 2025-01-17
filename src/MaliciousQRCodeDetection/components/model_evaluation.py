import os
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix, accuracy_score, roc_curve
import json
import pandas as pd
from tensorflow.keras.models import load_model
from MaliciousQRCodeDetection.logging.logger import logger
from MaliciousQRCodeDetection.exception import MaliciousQRException
from MaliciousQRCodeDetection.entity.config_entity import ModelEvaluationConfig


class ModelEvaluation:
    def __init__(self,config: ModelEvaluationConfig):
        self.config = config

    def metrics(self):

        train_df = pd.read_csv(self.config.train_data)
        test_df = pd.read_csv(self.config.test_data)
        model =  load_model(self.config.model_path)
        logger.info('Train data, test data and model loaded sucessfully ..')

        X_train = train_df.drop(columns=['result'])
        y_train = train_df['result']
        X_test = test_df.drop(columns=['result'])
        y_test = test_df['result']

        # Handle missing values
        logger.info(f"Number of NaNs in y_train: {y_train.isna().sum()}")
        logger.info(f"Number of NaNs in y_test: {y_test.isna().sum()}")
        logger.info(f"y_test shape: {y_test.shape}")

        y_train_pred = model.predict(X_train)
        y_test_pred = model.predict(X_test)

        y_train_binary = [0 if prob < 0.5 else 1 for prob in y_train_pred]
        y_test_binary = [0 if prob < 0.5 else 1 for prob in y_test_pred]

        train_json = {
            'Accuracy Score: ': accuracy_score(y_train,y_train_binary),        
        }

        test_json = {
            'Accuracy Score: ': accuracy_score(y_test,y_test_binary),
        }

        with open(self.config.train_metrics_file, 'w') as f:
            json.dump(train_json, f)

        with open(self.config.test_metrics_file, 'w') as f:
            json.dump(test_json, f)

        
        logger.info('Train & Test Metrics Json file saved sucessfully.')



