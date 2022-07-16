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
                 Heating_Load: float,
                 Cooling_Load: float):
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