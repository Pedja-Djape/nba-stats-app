from . import teams as teams_module
from . import apiBlueprint
from . import lib
from flask import request, abort, Response
from ..models import Player, Team, db
from .players import ALL_PLAYERS

@apiBlueprint.route("/players")
def getAllPlayers():
    players = Player.query.all()
    players = {player.playerName: player.playerID for player in players}
    return {'data': [players]}

@apiBlueprint.route("/players/<string:player_id>")
def getPlayer(player_id):
    player = Player.query.filter_by(id=player_id).first()
    if player == None:
        return {'status': "error", "message": f"No player exists with id '{player}'"}
    return {'status': "success", "data": {"id": player_id, "type": "player", "metadata": player} }

@apiBlueprint.route("/players/<string:player_id>",methods=["POST","PUT"])
def updatePlayer(player_id):
    player = Player.query.filter_by(player_id=player_id).scalar()
    args_dict = request.args.to_dict()
    if player == None and ('player_name' not in args_dict or 'current_team_id' not in args_dict):
        return {'status': "error", "message": f"Missing required information to create player."}
    # add player if not in table
    new_player = None
    if player == None:
        print("NOW HERE \n\n\n")
        new_player = Player(
            player_id=player_id,
            player_name=args_dict['player_name'],
            current_team_id=args_dict['current_team_id']
        )
        db.session.add(new_player)
    db.session.commit()
    return {"status": "success", "data": repr(new_player)}

@apiBlueprint.route("/teams",methods=["GET","POST"])
def getTeamsMapping():
    if request.method == "POST":
        for team in teams_module.teams:
            teamEntry = Team(team_id=team[0],team_abb=team[1],team_name=team[-1])
            db.session.add(teamEntry)
        db.session.commit()
        rval = Team.query.all()
        return {"status": "success", 'data': rval}
    teams = Team.query.all()
    return teams


@apiBlueprint.route("/teams/<string:teamID>/roster")
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

@apiBlueprint.route("/delete")
def dle():
    db.session.query(Player).delete()
    db.session.commit()
    return {"status": "success"}


    
