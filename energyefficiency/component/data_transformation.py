from energyefficiency.exception import HeatCoolException
from energyefficiency.logger import logging
from energyefficiency.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig
from energyefficiency.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
import sys,os

class DataTransformation:

    def __init__(self,data_transformation_config: DataTransformationConfig,
                 data_ingestion_artifact: DataIngestionArtifact,
                 data_validation_artifact: DataValidationArtifact
                 ):
        try:
            self.data_transformation_config = data_transformation_config
            self.data_ingestion_artifact = DataIngestionArtifact,
            self.data_validation_artifact = DataValidationArtifact
        except Exception as e:
            raise HeatCoolException(e,sys) from e