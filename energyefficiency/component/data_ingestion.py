from energyefficiency.entity.config_entity import DataIngestionConfig
from energyefficiency.exception import HeatCoolException
from energyefficiency.logger import logging
from energyefficiency.entity.artifact_entity import DataIngestionArtifact
import sys,os
import pandas as pd
import numpy as np
from six.moves import urllib

class Ingestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            logging.info(f"{'='*20} Data Ingestion log started.{'='*20}")
            self.data_ingestion_config = data_ingestion_config
        
        except Exception as e:
            raise HeatCoolException(e,sys) from e