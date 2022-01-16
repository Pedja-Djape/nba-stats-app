from time import process_time_ns
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

	def _modifyParams(self):
		for key in self.queryParams:
			assert key in self.baseParams
			if self.queryParams[key] != self.baseParams[key]:
				self.baseParams[key] = self.queryParams[key]
	
	def _formatResponse(self):
		if self.statusCode < 200 or self.statusCode > 299:
			print(self.response.content)
			self.response = None
		self.response = self.response.json()

	def makeRequest(self):
		self._modifyParams()
		self.response = req.get(url=self.url,
								params=self.baseParams,
								headers=REQUEST_HEADERS)
		self.statusCode = self.response.status_code
		self._formatResponse()
		self.response = self.response["resultSets"]
	
	def getResponseObj(self):
		return self.response
	
	def getHeadersMapping(self,headers):
		mapping = {k: v for v,k in enumerate(headers)}
		return mapping
	


class teamsMetadataRequest(statsRequest):
	def __init__(self,queryParams,baseParams = PLAYERS_PARAMS,resource = "playerindex"):
		super().__init__(resource, queryParams=queryParams,baseParams=baseParams)
	
	def getRoster(self):
		players = self.response[0]['rowSet']
		roster = {f"{player[2]} {player[1]}": player[0] for player in players}
		return roster

class playerCareerStatsRequest(statsRequest):
	def __init__(self, queryParams, baseParams = PLAYER_CAREER_STATS_PARAMS, resource="playercareerstats"):
		super().__init__(resource=resource,queryParams=queryParams,baseParams=baseParams)
		self._seasons = []
	
	def getSeasonsPlayed(self):
		assert self.response[0]['name'] == "SeasonTotalsRegularSeason"
		resp = self.response[0]
		for season in resp['rowSet']:
			self._seasons.append(season[1])
		return self._seasons

class playerShotchartRequest(statsRequest):
	def __init__(self, queryParams, baseParams = SHOTCHART_PARAMS, resource = "shotchartdetail"):
		super().__init__(resource=resource, queryParams=queryParams, baseParams=baseParams)

	def getPlayerShotchartResponse(self):
		resp = self.response[0]
		assert resp['name'] == 'Shot_Chart_Detail'
		headerMapping = self.getHeadersMapping(resp['headers'])
		data = resp['rowSet']
		return data,headerMapping

	


	




	
		

		
