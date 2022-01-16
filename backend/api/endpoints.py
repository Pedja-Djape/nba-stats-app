from . import teams
from . import apiBlueprint
from . import lib
from flask import request, abort 
from .players import ALL_PLAYERS
from backend import api


# @apiBlueprint.route("/teams")
# def getAllTeams():
#     return {'data': {"teams": teamsDict}}

# @apiBlueprint.route("/players")
# def getAllPlayers():
#     return {'data': {"players": ALL_PLAYERS}}

@apiBlueprint.route("/teams")
def getTeamsMapping():
    return teams.teamsDict

@apiBlueprint.route("/teams/<string:teamID>")
def getTeamRoster(teamID):
    argsDict = request.args.to_dict()
    argsDict['TeamID'] = teamID
    roster = lib.getTeamRoster(argsDict)
    return {
            "status": "success",
            "data": 
            {
                "id": teamID,
                "roster": roster
            }
        }

@apiBlueprint.route("/shotchart/player/<string:playerID>")
def getPlayShotchartData(playerID):
    argsDict = request.args.to_dict()
    argsDict['PlayerID'] = playerID
    playersc, _ = lib.getPlayerShotchartAvg(reqArgs=argsDict)
    return {
        "status": "success",
        'data': 
            {
                'playerShotchartData': playersc
            }  
    }

    
