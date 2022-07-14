from energyefficiency.exception import HeatCoolException
from energyefficiency.logger import logging
import os,sys



class ModelFactory:
    def __init__(self, model_config_path: str = None):
        try:
            pass
        except Exception as e:
            raise HeatCoolException(e,sys) from e