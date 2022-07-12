from evidently import dashboard
from energyefficiency.exception import HeatCoolException
from energyefficiency.logger import logging
from energyefficiency.entity.config_entity import DataIngestionConfig, DataValidationConfig
from energyefficiency.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
import sys,os
from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection
import pandas as pd
import json
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab

class DataValidation:
    
    def __init__(self,data_validation_config:DataValidationConfig,
                data_ingestion_artifact: DataIngestionArtifact):
        try:
            logging.info(f"{'='*20} Data Validation log started. {'='*20}")
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

    def get_train_and_test_df(self):
        try:
            train_df = pd.read_excel(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_excel(self.data_ingestion_artifact.test_file_path)
            return train_df, test_df
        except Exception as e:
            raise HeatCoolException(e,sys) from e

    def validate_dataset_schema(self)->bool:
        try:
            validation_status = False
            validation_status = True
            return validation_status
        except Exception as e:
            raise HeatCoolException(e,sys) from e

    def get_and_save_data_drift_report(self):
        try:
            profile = Profile(sections=[DataDriftProfileSection()])

            train_df,test_df = self.get_train_and_test_df()

            profile.calculate(train_df,test_df)

            profile.json()

            report = json.loads(profile.json())

            report_file_path = self.data_validation_config.report_file_path

            report_dir = os.path.dirname(report_file_path)

            os.makedirs(report_dir,exist_ok=True)

            with open(report_file_path,"w") as report_file:
                json.dump(report,report_file,indent=6)
            return report
        except Exception as e:
            raise HeatCoolException(e,sys) from e

    def save_data_drift_report_page(self):
        try:
            dashboard = Dashboard(tabs = [DataDriftTab()])
            train_df,test_df = self.get_train_and_test_df()
            dashboard.calculate(train_df,test_df)

            report_page_file_path = self.data_validation_config.report_page_file_path

            report_page_dir = os.path.dirname(report_page_file_path)

            os.makedirs(report_page_dir,exist_ok=True)

            dashboard.save(report_page_file_path)
        except Exception as e:
            raise HeatCoolException(e,sys) from e

    def is_data_drift_found(self)->bool:
        try:
            report = self.get_and_save_data_drift_report()
            self.save_data_drift_report_page()
            return True
        except Exception as e:
            raise HeatCoolException(e,sys) from e

    def initiate_data_validation(self)-> DataValidationArtifact:
        try:
            self.is_train_test_file_exists()
            self.validate_dataset_schema()
            self.is_data_drift_found()

            data_validation_artifact = DataValidationArtifact(
                schema_file_path=self.data_validation_config.schema_file_path,
                report_file_path=self.data_validation_config.report_file_path,
                report_page_file_path=self.data_validation_config.report_page_file_path,
                is_validated=True,
                message="Data Validation performed successfully")
            logging.info(f"data_validation_artifact: {data_validation_artifact}")
            return data_validation_artifact
        except Exception as e:
            raise HeatCoolException(e,sys) from e

    def __del__(self):
            logging.info(f"{'='*20}Data Validation log completed.{'='*20} \n\n")