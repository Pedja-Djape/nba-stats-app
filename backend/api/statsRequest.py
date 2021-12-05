import requests as req
from .requestParams import *
from copy import deepcopy

class statsRequestBase:
	def __init__(self,headers=None) -> None:
		self.response = None
		if headers == None:
			self.headers = REQUEST_HEADERS
		
		self.baseURL = "https://stats.nba.com/stats/"


class statsRequest(statsRequestBase):

	def __init__(self,resource,queryParams,baseParams):
		super().__init__()
		self.resource    = resource
		self.url         = self.baseURL + self.resource
		self.queryParams = queryParams
		self.baseParams  = deepcopy(baseParams)
		self.statusCode  = None

	def makeRequest(self):
		self.modifyParams()
		self.response = req.get(url=self.url,
								params=self.baseParams,
								headers=REQUEST_HEADERS)
		self.statusCode = self.response.status_code

	def getResponseObj(self):
		return self.response
	
	def modifyParams(self):
		for key in self.queryParams:
			assert key in PLAYERS_PARAMS
			if self.queryParams[key] != PLAYERS_PARAMS[key]:
				self.baseParams[key] = self.queryParams[key]
		

class teamsMetadataRequest(statsRequest):
	def __init__(self,queryParams,baseParams = PLAYERS_PARAMS,resource = "playerindex"):
		super().__init__(resource, queryParams=queryParams,baseParams=baseParams)

	def formatResponse(self):
		respObj = self.response.json()
		players = respObj['resultSets'][0]['rowSet']
		roster = {f"{player[2]} {player[1]}": player[0] for player in players}
		return roster




	




	
		

		
