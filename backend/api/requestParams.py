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

