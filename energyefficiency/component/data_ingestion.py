from energyefficiency.entity.config_entity import DataIngestionConfig
from energyefficiency.exception import HeatCoolException
from energyefficiency.logger import logging
from energyefficiency.entity.artifact_entity import DataIngestionArtifact
import sys,os
import pandas as pd
import numpy as np
from six.moves import urllib
import urllib.request
from sklearn.model_selection import StratifiedShuffleSplit

class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            logging.info(f"{'='*20} Data Ingestion log started.{'='*20}")
            self.data_ingestion_config = data_ingestion_config
        
        except Exception as e:
            raise HeatCoolException(e,sys) from e

    def download_energyefficiency_data(self) -> str:
        try:
            #Extracting remote url to download dataset
            download_url = self.data_ingestion_config.dataset_download_url

            #Folder location to download file
            raw_data_dir = self.data_ingestion_config.raw_data_dir

            if os.path.exists(raw_data_dir):
                os.remove(raw_data_dir)

            os.makedirs(raw_data_dir,exist_ok=True)

            energyefficiency_file_name = os.path.basename(download_url)

            raw_file_path = os.path.join(raw_data_dir,energyefficiency_file_name)

            logging.info(f"Downloading file from: [{download_url}] into :[{raw_data_dir}]")
            urllib.request.urlretrieve(download_url,raw_file_path)
            logging.info(f"File: [{raw_data_dir}] has been downloaded successfully.")
            return raw_file_path
        except Exception as e:
            raise HeatCoolException(e,sys) from e

    def split_data_as_train_test(self) -> DataIngestionArtifact:
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir

            file_name = os.listdir(raw_data_dir)[0]

            energyefficiency_file_path = os.path.join(raw_data_dir,file_name)

            logging.info(f"Reading excel file: [{energyefficiency_file_path}]")
            energyefficiency_data_frame = pd.read_excel(energyefficiency_file_path)

            energyefficiency_data_frame.rename(columns={'X1':"Relative_Compactness",'X2':"Surface_Area",
                                                'X3':"Wall_Area",'X4':"Roof_Area",'X5':"Overall_Height",
                                                'X6':"Orientation",'X7':"Glazing_Area",'X8':"Glazing_Area_Distribution",
                                                'Y1':"Heating_Load",'Y2':"Cooling_Load"},inplace=True
                                                )
            energyefficiency_data_frame["surface_area_cat"] = pd.cut(
                energyefficiency_data_frame["Surface_Area"],
                bins=[500.0,550.0,600.0,700.0,800.0,np.inf],
                labels = [1,2,3,4,5] #Group Category for Stratified Split
            )             

            logging.info(f"Splitting Data into train and test")
            strat_train_set = None
            strat_test_set = None

            split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

            for train_index, test_index in split.split(energyefficiency_data_frame,energyefficiency_data_frame["surface_area_cat"]):
                strat_train_set = energyefficiency_data_frame.loc[train_index].drop(["surface_area_cat"],axis=1)
                strat_test_set = energyefficiency_data_frame.loc[test_index].drop(["surface_area_cat"],axis=1)

            train_file_path = os.path.join(self.data_ingestion_config.ingested_train_dir,file_name)
            test_file_path = os.path.join(self.data_ingestion_config.ingested_test_dir,file_name)

            if strat_train_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_train_dir,exist_ok=True)
                logging.info(f"Exporting training dataset to file: [{train_file_path}]")
                strat_train_set.to_excel(train_file_path,index=False)

            if strat_test_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_test_dir,exist_ok=True)
                logging.info(f"Exporting test dataset to file: [{test_file_path}]")
                strat_test_set.to_excel(test_file_path,index=False)

            data_ingestion_artifact = DataIngestionArtifact(train_file_path=train_file_path,
                                                            test_file_path=test_file_path,
                                                            is_ingested=True,
                                                            message = f"Data Ingestion completed Successfully."
                                                            )
            logging.info(f"Data Ingestion Artifact: [{DataIngestionArtifact}]")
            return data_ingestion_artifact

        except Exception as e:
            raise HeatCoolException(e,sys) from e

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            raw_file_path = self.download_energyefficiency_data()
            return self.split_data_as_train_test()
        except Exception as e:
            raise HeatCoolException(e,sys) from e

    def __del__(self):
        logging.info(f"{'='*20}Data Ingestion log completed.{'='*20} \n\n")