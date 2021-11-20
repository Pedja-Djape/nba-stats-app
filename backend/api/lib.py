
from flask.ctx import _AppCtxGlobals
from . import apiBlueprint
from .teams import teamsDict
import requests as req
from flask import request, abort 
from players import ALL_PLAYERS

REQUEST_HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
        'Referer': 'https://stats.nba.com/',
        'Connection': 'keep-alive',
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://www.nba.com",
        "Referer": "https://www.nba.com/",
        'x-nba-stats-origin': 'stats',
        'x-nba-stats-token': 'true'
}

@apiBlueprint.route("/teams")
def getAllTeams():
    return {'data': {"teams": teamsDict}}

@apiBlueprint.route("/teams/<string:teamName>/id")
def getTeamID(teamName):
    if teamName not in teamsDict:
        abort(404)
    else:
        return {"data": {"id": teamsDict['teamName']}}

@apiBlueprint.route("/teams/<string:teamName/roster")
def getTeamRoster(teamName):
    if teamName not in teamsDict:
        abort(404)
    else:
        return {'data': "NOT_IMPLEMENTED"}

@apiBlueprint.route("/players/<string:playerName/id>")
def getPlayerID(playerName):
    if playerName not in ALL_PLAYERS:
        abort(404)
    else:
        return {"data": {"id": ALL_PLAYERS['playerName']} }
