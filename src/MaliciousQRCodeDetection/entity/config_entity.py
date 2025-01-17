from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    csv_dir: Path
    csv_file: str

@dataclass(frozen=True)
class FeatureEngineeringConfig:
    root_dir: Path
    csv_file: str
    train_data: str
    test_data: str
    scaler_file: str
    schema: dict

@dataclass
class DataValidationConfig:
    root_dir: Path
    status_file: str
    train_data: str
    test_data: str
    schema: dict
    status_file: str

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data: str
    test_data: str
    model_name: str


@dataclass
class ModelEvaluationConfig:
    root_dir: Path
    model_path: str
    train_data: str
    test_data: str
    train_metrics_file: str
    test_metrics_file: str

