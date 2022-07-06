from energyefficiency.config.configuration import Configuration
from energyefficiency.exception import HeatCoolException
from energyefficiency.logger import logging
from energyefficiency.entity.artifact_entity import DataIngestionArtifact
from energyefficiency.entity.config_entity import DataIngestionConfig
from energyefficiency.component.data_ingestion import DataIngestion
import sys,os

class Pipeline:

    def __init__(self,config:Configuration = Configuration()) -> None:
        try:
            self.config = config
        except Exception as e:
            raise HeatCoolException(e,sys) from e

    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise HeatCoolException(e,sys) from e

    def start_data_validation(self):
        pass

    def start_data_transformation(self):
        pass

    def start_model_trainer(self):
        pass

    def start_model_evaluation(self):
        pass

    def start_model_pusher(self):
        pass
    
    def run_pipeline(self):
        try:
            #Data Ingestion

            data_ingestion_artifact = self.start_data_ingestion()

        except Exception as e:
            raise HeatCoolException(e,sys) from e