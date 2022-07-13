from energyefficiency.exception import HeatCoolException
from energyefficiency.logger import logging
from energyefficiency.entity.config_entity import DataTransformationConfig
from energyefficiency.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact,DataTransformationArtifact
import sys,os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from energyefficiency.util.util import read_yaml_file,load_data,save_numpy_array_data,load_numpy_array_data,save_object,load_object, save_object
from energyefficiency.constant import *

  # Relative Compactness: float
  # Surface Area: float
  # Wall Area: float
  # Roof Area: float
  # Overall Height: float
  # Orientation: int
  # Glazing Area: float
  # Glazing Area Distribution: int
  # Heating Load: float
  # Cooling Load: float

class DataTransformation:
    
    def __init__(self, data_transformation_config:DataTransformationConfig, 
                 data_ingestion_artifact: DataIngestionArtifact,
                 data_validation_artifact: DataValidationArtifact):
        try:
            logging.info(f"{'='*20} Data Transformation log started. {'='*20}")
            self.data_transformation_config = data_transformation_config
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_artifact = data_validation_artifact
        except Exception as e:
            raise HeatCoolException(e,sys) from e

    def get_data_transformer_object(self)->ColumnTransformer:
        try:
            schema_file_path = self.data_validation_artifact.schema_file_path

            dataset_schema = read_yaml_file(file_path=schema_file_path)

            numerical_columns = dataset_schema[NUMERICAL_COLUMN_KEY]

            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessing = ColumnTransformer(transformers=[
                ('imputer', SimpleImputer(strategy="median"),numerical_columns),
                ('scaler', StandardScaler(),numerical_columns)
                ]
                )
            return preprocessing
        except Exception as e:
            raise HeatCoolException(e,sys) from e

    def initiate_data_transformation(self)->DataTransformationArtifact:
        try:
            logging.info(f"Obtained preprocessing object")
            preprocessing_obj = self.get_data_transformer_object()

            logging.info(f"Obtaining training and test file path.")
            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            schema_file_path = self.data_validation_artifact.schema_file_path

            logging.info("Loading training and test data as pandas dataframe.")
            train_df = load_data(file_path=train_file_path, schema_file_path=schema_file_path)

            test_df = load_data(file_path=test_file_path,schema_file_path=schema_file_path)

            schema = read_yaml_file(file_path = schema_file_path)

            target_column_name = schema[TARGET_COLUMN_KEY]

            logging.info(f"Splitting input and target feature from training and testing dataframe.")
            input_feature_train_df = train_df.drop(columns=target_column_name,axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=target_column_name,axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info(f"Applying preprocessing object on training dataframe and testing dataframe")
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]

            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            transformed_train_dir = self.data_transformation_config.transformed_train_dir
            transformed_test_dir = self.data_transformation_config.transformed_test_dir

            train_file_name = os.path.basename(train_file_path).replace(".xlsx",".npz")
            test_file_name = os.path.basename(test_file_path).replace(".xlsx",".npz")

            transformed_train_file_path = os.path.join(transformed_train_dir, train_file_name)
            transformed_test_file_path = os.path.join(transformed_test_dir, test_file_name)

            logging.info(f"Saving transformed training and testing array in artifact array.")
            save_numpy_array_data(file_path = transformed_train_file_path, array=train_arr)
            save_numpy_array_data(file_path = transformed_test_file_path, array=test_arr)

            preprocessing_obj_file_path = self.data_transformation_config.preprocessed_object_file_path

            logging.info(f"Saving preprocessing object")
            save_object(file_path=preprocessing_obj_file_path, obj=preprocessing_obj)

            data_transformation_artifact = DataTransformationArtifact(is_transformed=True,
                                           message="Data Transformation Successful",
                                           transformed_train_file_path=transformed_train_file_path,
                                           transformed_test_file_path=transformed_test_file_path,
                                           preprocessed_object_file_path=preprocessing_obj_file_path
                                           )
            logging.info(f"Data transformation artifact: [{data_transformation_artifact}]")
            return data_transformation_artifact
        except Exception as e:
            raise HeatCoolException(e,sys) from e

    def __del__(self):
            logging.info(f"{'='*20}Data Transformation log completed.{'='*20} \n\n")