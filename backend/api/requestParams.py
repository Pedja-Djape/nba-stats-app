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

import requests as req

SHOTCHART_PARAMS = {
    'AheadBehind': '',
    'ClutchTime': '',
    'ContextFilter': "SEASON_YEAR='2020-21'",
    'ContextMeasure': "FGA",
    'DateFrom': '',
    'DateTo': '',
    'EndPeriod': 10,
    'EndRange': 28800,
    'GameID': '',
    'GameSegment': '',
    'LastNGames': 0,
    'LeagueID': "00",
    'Location': '',
    'Month': 0,
    'OpponentTeamID': 0,
    'Outcome': '',
    'Period': 0,
    'PlayerID': None,
    'PointDiff': '',
    'PlayerPosition': '',
    'RangeType': 0,
    'RookieYear': '',
    'Season': "2020-21",
    'SeasonSegment': '',
    'SeasonType': "Regular Season",
    'StartPeriod': 1,
    'StartRange': 0,
    'TeamID': 0,
    'VsConference': '',
    'VsDivision': ''
}



# r = req.get("https://stats.nba.com/stats/shotchartdetail?AheadBehind=&CFID=33&CFPARAMS=2020-21&ClutchTime=&Conference=&ContextFilter=&ContextMeasure=FGA&DateFrom=&DateTo=&Division=&EndPeriod=10&EndRange=28800&GROUP_ID=&GameEventID=&GameID=&GameSegment=&GroupID=&GroupMode=&GroupQuantity=5&LastNGames=0&LeagueID=00&Location=&Month=0&OnOff=&OpponentTeamID=0&Outcome=&PORound=0&Period=0&PlayerID=203507&PlayerID1=&PlayerID2=&PlayerID3=&PlayerID4=&PlayerID5=&PlayerPosition=&PointDiff=&Position=&RangeType=0&RookieYear=&Season=2020-21&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StartPeriod=1&StartRange=0&StarterBench=&TeamID=0&VsConference=&VsDivision=&VsPlayerID1=&VsPlayerID2=&VsPlayerID3=&VsPlayerID4=&VsPlayerID5=&VsTeamID=",
#     headers=REQUEST_HEADERS)

# print(r.content)