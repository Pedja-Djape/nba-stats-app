from . import db



class Player(db.Model):
    __tablename__ = 'players'
    __table_args__ = {'schema': 'nba'}

    player_id = db.Column(db.String(256),primary_key=True)
    player_name = db.Column(db.String(256))
    current_team_id = db.Column(db.String(256))

    def __repr__(self) -> str:
        return f"<Player(player_id='{self.player_id}', player_name='{self.player_name}', current_team_id='{self.current_team_id}')"

class Team(db.Model):
    __tablename__ = 'team'
    __table_args__ = {'schema': 'nba'}
    
    team_name = db.Column(db.String(256),unique=True)
    team_id = db.Column(db.String(256),primary_key=True)
    team_abb = db.Column(db.String(3),unique=True)


    def __repr__(self) -> str:
        return f"Team(team_name='{self.team_name}', team_id={self.team_id}, team_abb={self.team_abb})"

