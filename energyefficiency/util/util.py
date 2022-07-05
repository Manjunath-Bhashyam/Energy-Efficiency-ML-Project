import yaml
from energyefficiency.exception import HeatCoolException
import sys,os

def read_yaml_file(file_name:str)->dict:
    """
    Function reads a YAML file and returns the contents as a dictionary.
    file_name: str
    """
    try:
        with open(file_name,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HeatCoolException(e,sys) from e