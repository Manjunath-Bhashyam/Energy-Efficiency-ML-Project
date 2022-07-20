from energyefficiency.pipeline.pipeline import Pipeline
from energyefficiency.logger import logging
from energyefficiency.exception import HeatCoolException
from energyefficiency.config.configuration import Configuration
import sys,os
from energyefficiency.component.data_transformation import DataTransformation

def main():
    try:
        config_path = os.path.join("config","config.yaml")
        pipeline = Pipeline(Configuration(config_file_path=config_path))
        #pipeline.run_pipeline()
        pipeline.start()
        logging.info("main function execution completed.")
        # data_validation_config = Configuration().get_data_validation_config()
        # print(data_validation_config)
        # data_transformation_config = Configuration().get_data_transformation_config()
        # print(data_transformation_config)
        # schema_file_path = r"D:\Energy Efficiency ML\Energy-Efficiency-ML-Project\config\schema.yaml"
        # file_path = r"D:\Energy Efficiency ML\Energy-Efficiency-ML-Project\energyefficiency\artifact\data_ingestion\2022-07-08_23-42-58\ingested_data\train\ENB2012_data.xlsx"

        # df = DataTransformation.load_data(file_path=file_path, schema_file_path=schema_file_path)
        # print(df.columns,df.dtypes)

    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__ == "__main__":
    main()
