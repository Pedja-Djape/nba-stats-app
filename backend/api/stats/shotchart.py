import pandas as pd
import numpy as np
from . import utils

SHOTCHART_TYPES = {"ZONE","HEX"}

def getShotchartData(rawData,mapping,scType="HEX"):
    if scType not in SHOTCHART_TYPES:
        raise ValueError(f"Value for 'scType' is not a valid shotchart type: {scType}")
    columns = ["LOC_X","LOC_Y","SHOT_ATTEMPTED_FLAG","SHOT_MADE_FLAG"]
    if scType == "ZONE":
        columns = ["SHOT_ZONE_BASIC","SHOT_ZONE_AREA","SHOT_ZONE_RANGE","SHOT_DISTANCE","SHOT_ATTEMPTED_FLAG","SHOT_MADE_FLAG"]
    
    df = utils.genDataframeFromRawData(rawData,columns,mapping)
    return df

def getCareerShotchartData(seasons,careerRawData,mapping,scType='HEX'):
    cumData = []
    for season in seasons:
        cumData += careerRawData[season]
    
    df = getShotchartData(cumData,mapping,scType)
    return df

def getCareerShotchartZoneAvgs(careerDataframe): 
    x = careerDataframe.groupby(by=["SHOT_ZONE_BASIC","SHOT_ZONE_AREA","SHOT_ZONE_RANGE"],as_index=False)
    y = x.mean()
    y.drop(columns=["SHOT_DISTANCE","SHOT_ATTEMPTED_FLAG"],inplace=True)
    y.rename(columns={"SHOT_MADE_FLAG": "FG_PCT"},inplace=True)
    return y
