from energyefficiency.exception import HeatCoolException
from energyefficiency.logger import logging
from energyefficiency.entity.config_entity import DataIngestionConfig, DataValidationConfig
from energyefficiency.entity.artifact_entity import DataIngestionArtifact
import sys,os

class DataValidation:
    
    def __init__(self,data_validation_config:DataValidationConfig,
                data_ingestion_artifact: DataIngestionArtifact):
        try:
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact

        except Exception as e:
            raise HeatCoolException(e,sys) from e
    
    def is_train_test_file_exists(self)->bool:
        try:
            logging.info("Checking if train and test file is available")
            is_train_file_exist = False
            is_test_file_exist = False

            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            is_train_file_exist = os.path.exists(train_file_path)
            is_test_file_exist = os.path.exists(test_file_path)

            is_available = is_train_file_exist and is_test_file_exist

            logging.info(f"Is train and test file exists-> {is_available}")

            if not is_available:
                train_file = self.data_ingestion_artifact.train_file_path
                test_file = self.data_ingestion_artifact.test_file_path
                message = f"train file: {train_file} or test file: {test_file}" \
                    "is not present"
                raise Exception(message)
                
            return is_available
            
        except Exception as e:
            raise HeatCoolException(e,sys) from e

    def validate_dataset_schema(self)->bool:
        try:
            validation_status = False


            validation_status = True
            return validation_status
        except Exception as e:
            raise HeatCoolException(e,sys) from e


    def initiate_data_validation(self):
        try:
            self.is_train_test_file_exists()
            self.validate_dataset_schema()


        except Exception as e:
            raise HeatCoolException(e,sys) from e

