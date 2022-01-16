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



if __name__ == "__main__":
    with open("lbj.txt","r") as myfile:
        data = myfile.read()
    

    mapping = {
        'GRID_TYPE': 0, 
        'GAME_ID': 1, 
        'GAME_EVENT_ID': 2, 
        'PLAYER_ID': 3, 
        'PLAYER_NAME': 4, 
        'TEAM_ID': 5, 
        'TEAM_NAME': 6, 
        'PERIOD': 7, 
        'MINUTES_REMAINING': 8, 
        'SECONDS_REMAINING': 9, 
        'EVENT_TYPE': 10,
        'ACTION_TYPE': 11, 
        'SHOT_TYPE': 12, 
        'SHOT_ZONE_BASIC': 13, 
        'SHOT_ZONE_AREA': 14, 
        'SHOT_ZONE_RANGE': 15, 
        'SHOT_DISTANCE': 16, 
        'LOC_X': 17, 
        'LOC_Y': 18, 
        'SHOT_ATTEMPTED_FLAG': 19, 
        'SHOT_MADE_FLAG': 20, 
        'GAME_DATE': 21, 
        'HTM': 22, 
        'VTM': 23
    }

    data = eval(data)

    seasons = list(data.keys())
    x = getCareerShotchartData(seasons,data,mapping,scType="ZONE")
    y = getCareerShotchartZoneAvgs(x)
