from energyefficiency.pipeline.pipeline import Pipeline
from energyefficiency.logger import logging
from energyefficiency.exception import HeatCoolException
from energyefficiency.config.configuration import Configuration
import sys,os

def main():
    try:
        # pipeline = Pipeline()
        # pipeline.run_pipeline()
        # data_validation_config = Configuration().get_data_validation_config()
        # print(data_validation_config)
        data_transformation_config = Configuration().get_data_transformation_config()
        print(data_transformation_config)
    except Exception as e:
        logging.error(f"{e}")
        raise HeatCoolException(e,sys) from e


if __name__ == "__main__":
    main()
