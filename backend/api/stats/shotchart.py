import pandas as pd
import numpy as np
from . import utils
from ..statsRequest import playerShotchartRequest

SHOTCHART_TYPES = {"ZONE","HEX"}

class Shotchart:
    """
        This class is used to create a visual replresentation of a players shooting 
        efficiency from different regions on the court -- either a hex-plot or a zonal-plot.
    """
    def __init__(self,req_args=None, raw_data=None, mapping=None, shotchart_type="HEX"): 
        if shotchart_type not in SHOTCHART_TYPES:
            raise ValueError(f"Value for 'scType' is not a valid shotchart type: {shotchart_type}")
        self.type = shotchart_type
        self.raw_data = raw_data
        self.mapping = mapping
        self.columns = ["LOC_X","LOC_Y","SHOT_ATTEMPTED_FLAG","SHOT_MADE_FLAG"]
        self.df = self.__gen_shotchart_df(req_args=req_args)
        
    
    def __gen_shotchart_df(self,req_args=None):
        if self.type == "ZONE":
            self.columns = ["SHOT_ZONE_BASIC","SHOT_ZONE_AREA","SHOT_ZONE_RANGE",
                            "SHOT_DISTANCE","SHOT_ATTEMPTED_FLAG","SHOT_MADE_FLAG"]
        # if no request args passed --> the shotchart is in the database
        in_db = (req_args == None)
        if in_db:
            # generate df for shotchart
            df = utils.genDataframeFromRawData(self.rawData,self.columns,self.mapping)
        else:
            assert req_args != None
            # request object
            # del req_args['shotchart_type']
            shotchart_req = playerShotchartRequest(queryParams=req_args)
            # raw data --> list of all shots (shot is a list)
            data = shotchart_req.get_raw_data()
            # map heading to index in shot
            header_mapping = shotchart_req.get_header_mapping()
            # generate df for shot chart
            df = utils.genDataframeFromRawData(data,self.columns,header_mapping)
        return df

    def get_zone_avgs(self):
        # can only return zone averages for zonal type shotchart
        if self.type != "ZONE":
            return None
        # group df by all shot combinations
        shot_groups = self.df.groupby(by=["SHOT_ZONE_BASIC","SHOT_ZONE_AREA","SHOT_ZONE_RANGE"],as_index=False)
        # get mean for each shot type
        shot_group_avgs = shot_groups.mean()
        # drop misc columns
        shot_group_avgs.drop(columns=["SHOT_DISTANCE","SHOT_ATTEMPTED_FLAG"],inplace=True)
        shot_group_avgs.rename(columns={"SHOT_MADE_FLAG": "FG_PCT"},inplace=True)

        return shot_group_avgs
    
    def get_df(self):
        return self.df 
    

