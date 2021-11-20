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
    "AheadBehind": '',
    "ClutchTime": '',
    "ContextFilter": "",
    "ContextMeasure": 'PTS',
    "DateFrom": '',
    "DateTo": '',
    "EndPeriod": '',
    "EndRange": '',
    "GameID": '',
    "GameSegment": '',
    "LastNGames": '0',
    "LeagueID": '00',
    "Location": '',
    "Month": '0',
    "OpponentTeamID": '0',
    "Outcome": '',
    "Period": '0',
    "PlayerID": '203507',
    "PlayerPosition": '',
    "PointDiff": '',
    "Position": '',
    "RangeType": '',
    "RookieYear": '',
    "Season": '2018-19',
    "SeasonSegment": '',
    "SeasonType": "Regular Season",
    "StartPeriod": '',
    "StartRange": '',
    "TeamID": '0',
    "VsConference": '',
    "VsDivision": ''
}


