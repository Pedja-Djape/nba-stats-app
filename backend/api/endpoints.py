from . import teams
from . import apiBlueprint
from flask import request, abort 
from players import ALL_PLAYERS
from .lib import *

@apiBlueprint.route("/teams")
def getAllTeams():
    return {'data': {"teams": teamsDict}}

@apiBlueprint.route("/teams/<string:teamName>")
def getTeamInfo(teamName):
    if teamName not in teamsDict:
        abort(404)
    else:
        argsDict = request.args.to_dict()
        argsDict['TeamID'] = teamsDict[teamName]
        teamInfo = teamsMetadataRequest(queryParams=argsDict)
        teamInfo.makeRequest()
        roster = teamInfo.formatResponse() if teamInfo.statusCode == 200 else None
        return {
                "data": 
                {
                    "id": teamsDict[teamName],
                    "roster": roster
                }
            }

@apiBlueprint.route("/players/<string>:playerName/id")
def getPlayerID(playerName):
    pid = pidFromName(playerName)
    if pid is None:
        abort(404)
    else:
        return {"data": {"id": pid} }

print(getPlayerID("Carmelo Anthony"))




