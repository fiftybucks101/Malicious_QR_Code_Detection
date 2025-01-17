from MaliciousQRCodeDetection.constants import *
from MaliciousQRCodeDetection.utils.common import read_yaml, create_directories
from MaliciousQRCodeDetection.entity.config_entity import *

class ConfigurationManager:
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            schema_filepath = SCHEMA_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL=config.source_URL,
            csv_dir = config.csv_dir,
            csv_file = config.csv_file
        )

        return data_ingestion_config
    
    def get_feature_engineering_config(self) -> FeatureEngineeringConfig:
        config = self.config.feature_engineering
        schema = self.schema

        create_directories([config.root_dir])

        feature_engineering_config = FeatureEngineeringConfig(
            root_dir = config.root_dir,
            csv_file=config.csv_file,
            train_data = config.train_data,
            test_data = config.test_data,
            scaler_file = config.scaler_file,
            schema = schema
        )

        return feature_engineering_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            status_file = config.status_file,
            schema = schema,
            train_data = config.train_data,
            test_data=config.test_data
        )

        return data_validation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:

        config = self.config.model_training

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data=config.train_data,
            test_data=config.test_data,
            model_name=config.model_name,)
        
        return model_trainer_config
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir = config.root_dir,
            model_path = config.model_path,
            train_data = config.train_data,
            test_data=config.test_data,
            train_metrics_file=config.train_metrics_file,
            test_metrics_file=config.test_metrics_file,
          
        )

        return model_evaluation_config
    
    