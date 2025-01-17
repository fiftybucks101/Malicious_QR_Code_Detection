import os
from MaliciousQRCodeDetection.entity.config_entity import ModelTrainerConfig
import tensorflow
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation
from keras.callbacks import ModelCheckpoint
from tensorflow.keras.regularizers import l2
import pandas as pd
from MaliciousQRCodeDetection.logging.logger import logger
from MaliciousQRCodeDetection.exception import MaliciousQRException
import sys

class ModelTrainer:
    def __init__ (self, config: ModelTrainerConfig):
        self.config = config

    def Train(self):

        train_data = pd.read_csv(self.config.train_data)
        logger.info('Train data read Successfully')

        X_train = train_data.drop(columns=['result'])
        y_train = train_data['result']

        model = Sequential()

        model.add(Dense(32, activation='relu', input_shape=(23,), kernel_regularizer=l2(0.01)))
        model.add(Dropout(0.2))  
        
        model.add(Dense(16, activation='relu', kernel_regularizer=l2(0.01)))        
        model.add(Dropout(0.2))  

        model.add(Dense(8, activation='relu', kernel_regularizer=l2(0.01)))   
        model.add(Dropout(0.2))  

        model.add(Dense(1, activation='sigmoid'))

        model.compile(optimizer= 'adam',loss='binary_crossentropy',metrics=['acc'])

        checkpointer = ModelCheckpoint(
            self.config.model_name,    # Filepath to save the model
            monitor='val_acc',    # Metric to monitor for improvement
            mode='max',           # Save model when the monitored metric is maximized
            verbose=2,            # Print messages when saving the model
            save_best_only=True,   # Only save the model if it's the best so far
        )


        history=model.fit(X_train, y_train, batch_size=128, epochs=10, validation_split=0.2 , callbacks=[checkpointer])
        logger.info('Model Training Completed ......')
