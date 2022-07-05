import yaml
from energyefficiency.exception import HeatCoolException
import sys,os

def read_yaml_file(file_path:str)->dict:
    """
    Function reads a YAML file and returns the contents as a dictionary.
    file_path: str
    """
    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HeatCoolException(e,sys) from e