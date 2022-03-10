from unittest import skip
from .players import ALL_PLAYERS
from .teams import teamsDict
from .requestParams import *
from . import statsRequest
from backend.api import players
from .stats import shotchart

def getTeamID(teamName):
    if teamName not in teamsDict:
        return None
    return teamsDict[teamName]

def getTeamRoster(reqArgs=None):
    if reqArgs == None:
        return 
    teamMetadata = statsRequest.teamsMetadataRequest(queryParams=reqArgs)
    teamMetadata.makeRequest()
    roster = teamMetadata.getRoster()
    return teamMetadata

def getPlayerSeasons(playerID=None):
    if playerID == None:
        return 
    careerStatsRequest = statsRequest.playerCareerStatsRequest({
        "LeagueID": "00",
        "PerMode": "PerGame",
        "PlayerID": playerID
    })
    careerStatsRequest.makeRequest()
    seasons = careerStatsRequest.getSeasonsPlayed()
    return seasons


def getPlayerSeasonShotchart(reqArgs=None):
    if reqArgs == None:
        return
    playerSeasonSC = statsRequest.playerShotchartRequest(queryParams=reqArgs)
    playerSeasonSC.makeRequest()
    data,mapping = playerSeasonSC.getPlayerShotchartResponse()
    return data,mapping
    

def getPlayerShotchartRawData(reqArgs=None):
    if reqArgs == None:
        return    
    if "Career" not in reqArgs:
        data, headerMapping = getPlayerSeasonShotchart(reqArgs=reqArgs)
        return data, headerMapping
    del reqArgs["Career"]
    seasons = getPlayerSeasons(playerID=reqArgs["PlayerID"])
    data = {}
    headerMapping = None
    for season in seasons:
        reqArgs["Season"] = season
        pssc, headerMapping = getPlayerSeasonShotchart(reqArgs)
        data[season] = pssc

    return data,headerMapping


def getPlayerShotchartAvg(reqArgs=None):
    if reqArgs == None:
        return
    rval = getPlayerShotchartRawData(reqArgs)
    if rval == None:
        return
    data,headerMapping = rval
    seasons = list(data.keys())
    df = shotchart.getCareerShotchartData(seasons,data,headerMapping,scType='ZONE')
    df = shotchart.getCareerShotchartZoneAvgs(df)
    return df,headerMapping

