from . import db
from json import dumps

class Team(db.Model):
    __table_args__ = {'schema': 'nba'}
    
    id = db.Column(db.String(60),primary_key=True)
    name = db.Column(db.String(60),unique=True)
    abb = db.Column(db.String(3),unique=True)
    players = db.relationship('Player',backref='team')


    def __repr__(self) -> str:
        return dumps(self.as_dict())
    
    def as_dict(self):
        team_dict = {'name': self.name, 'id': self.id, 'abb': self.abb}
        return team_dict


class Player(db.Model):
    __table_args__ = {'schema': 'nba'}

    id = db.Column(db.String(60),primary_key=True)
    name = db.Column(db.String(60))
    team_id = db.Column(db.String(60),db.ForeignKey('nba.team.id'))

    def __repr__(self) -> str:
        player_dict = {'id': self.id, 'name': self.name, 'team_id': self.team_id}
        return dumps(player_dict)
    
    def as_dict(self):
        player_dict = {'id': self.id, 'name': self.name, 'team_id': self.team_id}
        return player_dict
    
class Shotchart(db.Model):
    __table_args__ = {'schema': 'nba',}

    player_id           = db.Column(db.String, primary_key=True)
    season_id           = db.Column(db.String, primary_key=True)
    team_id             = db.Column(db.String, primary_key=True)
    shot_zone_basic     = db.Column(db.String, nullable=False)
    shot_zone_area      = db.Column(db.String, nullable=False)
    shot_zone_range     = db.Column(db.String, nullable=False)
    shot_distance       = db.Column(db.String, nullable=False)
    field_goal_pct      = db.Column(db.String, nullable=False)
    num_shots           = db.Column(db.String, nullable=False)
