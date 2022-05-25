from .players import ALL_PLAYERS
from .teams import teamsDict
from .requestParams import *
from . import statsRequest
# from backend.api import players
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
    player_sc = shotchart.Shotchart(req_args=reqArgs,sc_type="ZONE")
    sc_df = player_sc.get_zone_avgs()

    print(sc_df)
    print(sc_df.to_json())
    return True




