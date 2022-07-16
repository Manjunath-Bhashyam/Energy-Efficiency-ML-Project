from energyefficiency.exception import HeatCoolException
from energyefficiency.logger import logging
from energyefficiency.entity.config_entity import ModelTrainerConfig
from energyefficiency.entity.artifact_entity import DataTransformationArtifact, ModelTrainerArtifact
from energyefficiency.entity.model_factory import ModelFactory
from energyefficiency.constant import *
from energyefficiency.util.util import read_yaml_file, load_data, load_numpy_array_data, save_numpy_array_data, save_object
import os,sys
import numpy as np
import pandas as pd
from typing import List

class HousingEstimatorModel:
    def __init__(self, preprocessing_object, trained_model_object):
        """
        TrainedModel Constructor
        preprocessing_object: preprocessing_object
        trained_model_object: trained_model_object
        """
        self.preprocessing_object = preprocessing_object
        self.trained_model_object = trained_model_object

    def predict(self, X):
        """
        function accepts raw inputs and then transformed raw input using preprocessing_object
        which guarantees that the inputs are in the same format as the training data
        At last it performs prediction on the transformed features 
        """
        transformed_feature = self.preprocessing_object.transform(X)
        return self.trained_model_object.predict(transformed_feature)

    def __repr__(self):
        return f"{type(self.trained_model_object).__name__}()"

    def __str__(self):
        return f"{type(self.trained_model_object).__name__}()"

class ModelTrainer:

    def __init__(self, model_trainer_config:ModelTrainerConfig, data_transformation_artifact:DataTransformationArtifact):
        try:
            logging.info(f"{'='*30} Model Trainer log started. {'='*30}")
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifact = data_transformation_artifact
        except Exception as e:
            raise HeatCoolException(e,sys) from e

    def initiate_model_trainer(self)->ModelTrainerArtifact:
        try:
            logging.info(f"Loading transformed training dataset")
            transformed_train_file_path = self.data_transformation_artifact.transformed_train_file_path
            train_array = load_numpy_array_data(file_path=transformed_train_file_path)

            logging.info(f"Loading transformed testing dataset")
            transformed_test_file_path = self.data_transformation_artifact.transformed_test_file_path
            test_array = load_numpy_array_data(file_path=transformed_test_file_path)
            
            logging.info(f"Splitting training and testing input and target feature")
            X_train,y_train,X_test,y_test = train_array[:,:-2],train_array[:,-2],test_array[:,:-2],test_array[:,-2]

            logging.info(f"Extracting model config file path")
            model_config_file_path = self.model_trainer_config.model_config_file_path

            logging.info(f"Initializing model factory class using above model config file: {model_config_file_path}")
            model_factory = ModelFactory(model_config_file_path=model_config_file_path)



        except Exception as e:
            raise HeatCoolException(e,sys) from e


