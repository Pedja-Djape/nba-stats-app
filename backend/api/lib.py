
from .teams import teamsDict
from players import ALL_PLAYERS

def pidFromName(pName):
    if pName not in ALL_PLAYERS:
        return None
    return ALL_PLAYERS[pName]


