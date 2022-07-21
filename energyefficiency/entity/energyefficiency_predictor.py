from energyefficiency.exception import HeatCoolException
from energyefficiency.util.util import load_object
import os,sys
import pandas as pd

class EnergyEfficiencyData:

    def __init__(self,
                 Relative_Compactness: float,
                 Surface_Area: float,
                 Wall_Area: float,
                 Roof_Area: float,
                 Overall_Height: float,
                 Orientation: int,
                 Glazing_Area: float,
                 Glazing_Area_Distribution: int,
                 Heating_Load: float = None,
                 Cooling_Load: float = None):
        try:
            self.Relative_Compactness = Relative_Compactness,
            self.Surface_Area = Surface_Area,
            self.Wall_Area = Wall_Area,
            self.Roof_Area = Roof_Area,
            self.Overall_Height = Overall_Height,
            self.Orientation = Orientation,
            self.Glazing_Area = Glazing_Area,
            self.Glazing_Area_Distribution = Glazing_Area_Distribution,
            self.Heating_Load = Heating_Load,
            self.Cooling_Load = Cooling_Load
        except Exception as e:
            raise HeatCoolException(e,sys) from e

    def get_energyefficiency_data_as_dict(self):

        try:
            input_data = {
                "Relative_Compactness": [self.Relative_Compactness],
                "Surface_Area": [self.Surface_Area],
                "Wall_Area": [self.Wall_Area],
                "Roof_Area": [self.Roof_Area],
                "Overall_Height": [self.Overall_Height],
                "Orientation": [self.Orientation],
                "Glazing_Area": [self.Glazing_Area],
                "Glazing_Area_Distribution": [self.Glazing_Area_Distribution]}
            return input_data
        except Exception as e:
            raise HeatCoolException(e,sys) from e

    def get_energyefficiency_input_data_frame(self):

        try:
            energyefficiency_input_dict = self.get_energyefficiency_data_as_dict()
            return pd.DataFrame(energyefficiency_input_dict)
        except Exception as e:
            raise HeatCoolException(e,sys) from e

class EnergyEfficiencyPredictor:

    def __init__(self, model_dir: str):
        try:
            self.model_dir = model_dir
        except Exception as e:
            raise HeatCoolException(e,sys) from e

    def get_latest_model_path(self):
        try:
            folder_name = list(map(int, os.listdir(self.model_dir)))
            latest_model_dir = os.path.join(self.model_dir, f"{max(folder_name)}")
            file_name = os.listdir(latest_model_dir)[0]
            latest_model_path = os.path.join(latest_model_dir, file_name)
            return latest_model_path
        except Exception as e:
            raise HeatCoolException(e,sys) from e

    def predict(self, X):
        try:
            model_path = self.get_latest_model_path()
            model = load_object(file_path=model_path)
            output = model.predict(X)
            return output
        except Exception as e:
            raise HeatCoolException(e,sys) from e
            