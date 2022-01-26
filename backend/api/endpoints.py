from . import teams
from . import apiBlueprint
from . import lib
from flask import request, abort, Response
from ..models import Player, Team, db
from .players import ALL_PLAYERS

# @apiBlueprint.route("/teams")
# def getAllTeams():
#     return {'data': {"teams": teamsDict}}

@apiBlueprint.route("/players")
def getAllPlayers():
    players = Player.query.all()
    players = {player.playerName: player.playerID for player in players}
    return {'data': [players]}


@apiBlueprint.route("/player",methods=["POST","PUT"])
def updatePlayer():
    for player in ALL_PLAYERS:
        playerName = player
        playerID = ALL_PLAYERS[player]
        playerEntry = Player(playerID=playerID,playerName=playerName)
        db.session.add(playerEntry)
    db.session.commit()
    return {"status": "success"}
    


@apiBlueprint.route("/teams",methods=["GET","POST"])
def getTeamsMapping():
    if request.method == "POST":
        team = request.values.get('team')
        entry = Team(team=team)
        db.session.add(entry); db.session.commit()
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

    
