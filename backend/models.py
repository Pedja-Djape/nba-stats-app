from . import db



class Player(db.Model):
    __tablename__ = 'players'
    __table_args__ = {'schema': 'nba'}

    playerID = db.Column(db.String(256),primary_key=True)
    playerName = db.Column(db.String(256))

    def __repr__(self) -> str:
        return f"<Player(playerID='{self.playerID}', playerName='{self.playerName}')"

class Team(db.Model):
    __tablename__ = 'team'
    __table_args__ = {'schema': 'nba'}
    
    team = db.Column(db.String(256),primary_key=True)

    def __repr__(self) -> str:
        return f"Team(team='{self.team}')"

