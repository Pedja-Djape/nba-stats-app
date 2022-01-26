from ..players import ALL_PLAYERS
# from ..teams import
import requests
from time import sleep
host = "http://127.0.0.1:5000"
endpoint = "/api/player"
for player in ALL_PLAYERS:
    requests.post(f"{host}{endpoint}",params={"playerName": player,"playerID": ALL_PLAYERS[player]})
    # sleep(2)
    



