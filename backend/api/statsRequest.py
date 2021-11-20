import requests as req

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


class statsRequestBase:
	def __init__(self,headers=None) -> None:
		self.response = None
		if headers == None:
			self.headers = REQUEST_HEADERS
		
		self.baseURL = "https://stats.nba.com/stats/"
		

class statsRequest(statsRequestBase):

	def __init__(self,endpoint):
		super().__init__()
		self.endpoint = endpoint
		self.url = self.baseURL + self.endpoint
	
	def makeRequest(self):
		resp = req.get(url=self.url,params={"PlayerID": "203507",
		"TeamID": "0",
		"AheadBehind":"",
		"ClutchTime":"",
		"ContextFilter":"SEASON_YEAR='2020-21'",
		"ContextMeasure": "FGA",
		"DateFrom":"",
		"DateTo":"",
		"EndPeriod":10,
		"EndRange":28800,
		"GameID":"",
		"LastNGame":"",
		"LeagueID":"00",
		"Location":"",
		"Month":0,
		"OpponentTeamID":0,
		"Outcome":"",
		"Period":0,
		"PointDiff":"",
		"Position":"",
		"RangeType":"",
		"RookieYear":"",
		"Season":"2020-21",
		"SeasonSegment":"",
		"SeasonType":"Regular Season",
		"StartPeriod":1,
		"StartRange":0})

		print(resp)

print(statsRequest("/shotchartdetail","","").makeRequest())






	
		

		
