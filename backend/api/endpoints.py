from . import teams as teams_module
from . import apiBlueprint
from . import lib
from flask import request
from ..models import Player, Team, db

@apiBlueprint.route("/players")
def getAllPlayers():
    players = Player.query.all()
    players = {player.name: player.id for player in players}
    return {'data': [players], "status": "success"}

@apiBlueprint.route("/players/<string:id>")
def getPlayer(id):
    player = Player.query.filter_by(id=id).first()
    if player == None:
        return {'status': "error", "message": f"No player exists with id '{id}'"}
    return {'status': "success", "data": {"id": id, "type": "player", "metadata": player.as_dict()} }

@apiBlueprint.route("/players/<string:id>",methods=["POST","PUT"])
def updatePlayer(id):
    player = Player.query.filter_by(id=id).scalar()
    args_dict = request.args.to_dict()
    if player == None and ('player_name' not in args_dict or 'current_team_id' not in args_dict):
        return {'status': "error", "message": f"Missing required information to create player."}
    # add player if not in table
    if args_dict['current_team_id'] == 0:
        return {'status': 'error', "message": f"Player with id='{id}' and name={args_dict['player_name']} is not currently rostered."}
    if player == None:
        player = Player(
            id=id,
            name=args_dict['player_name'],
            team_id=args_dict['current_team_id']
        )
        db.session.add(player)
    else:
        if player.name != args_dict["player_name"]:
            player.name = args_dict["player_name"]
        if player.team_id != args_dict['current_team_id']:
            player.team_id = args_dict["current_team_id"]
    db.session.commit()
    return {"status": "success", "data": player.as_dict()}

@apiBlueprint.route("/teams",methods=["GET","POST"])
def getTeamsMapping():
    if request.method == "POST":
        for team in teams_module.teams:
            teamEntry = Team(id=team[0],abb=team[1],name=team[-1])
            db.session.add(teamEntry)
        db.session.commit()
        rval = Team.query.all()[0].as_dict()
        return {"status": "success", 'data': rval}
    teams = Team.query.all()
    if len(teams) > 0:
        teams = [team.as_dict() for team in teams]
    return {"status": "success", "data": teams}


@apiBlueprint.route("/teams/<string:id>/roster")
def getTeamRoster(id):
    team = Team.query.filter_by(id=id).first()
    roster = []
    for player in team.players:
        player_dict = player.as_dict()
        del player_dict['team_id']
        roster.append(player_dict)

    # roster = [player.as_dict() for player in team.players]
    rval = {"type": "team", "metadata": team.as_dict(),"roster": roster}
    return {"status": "success", "data": [rval]}
    
    
@apiBlueprint.route("/shotchart/player/<string:id>")
def getPlayShotchartData(id):
    argsDict = request.args.to_dict()
    argsDict['id'] = id
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


    
