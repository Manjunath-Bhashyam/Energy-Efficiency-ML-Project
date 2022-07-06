from energyefficiency.pipeline.pipeline import Pipeline
from energyefficiency.logger import logging
from energyefficiency.exception import HeatCoolException
import sys,os

def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
    except Exception as e:
        logging.error(f"{e}")
        raise HeatCoolException(e,sys) from e


if __name__ == "__main__":
    main()
