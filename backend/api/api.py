
from . import apiBlueprint
from .teams import teamsDict
import requests as req
from flask import request

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

@apiBlueprint.route("/stats")
def getStats():
    response = req.get(url="https://stats.nba.com/stats/shotchartdetail?AheadBehind=&ClutchTime=&ContextFilter=&ContextMeasure=PTS&DateFrom=&DateTo=&EndPeriod=&EndRange=&GameID=&GameSegment=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&Period=0&PlayerID=203507&PlayerPosition=&PointDiff=&Position=&RangeType=&RookieYear=&Season=&SeasonSegment=&SeasonType=Regular+Season&StartPeriod=&StartRange=&TeamID=0&VsConference=&VsDivision=",
    headers=REQUEST_HEADERS)
    print(response)
    return response.content


@apiBlueprint.route("/teams")
def getAllTeams():
    return teamsDict

@apiBlueprint.route("/teams/<string:team_name>")
def getTeamID(team_name):
    if team_name not in teamsDict:
        return {"team_not_found": -1}
    else:
        return {team_name: str(teamsDict[team_name])}
    
