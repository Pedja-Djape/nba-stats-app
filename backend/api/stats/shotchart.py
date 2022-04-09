import pandas as pd
import numpy as np
from . import utils
from ..statsRequest import playerShotchartRequest

SHOTCHART_TYPES = {"ZONE","HEX"}

class Shotchart:
    def __init__(self, raw_data=None, mapping=None, sc_type="HEX"): 
        if sc_type not in SHOTCHART_TYPES:
            raise ValueError(f"Value for 'scType' is not a valid shotchart type: {sc_type}")
        self.type = sc_type
        self.raw_data = raw_data
        self.mapping = mapping
        self.columns = ["LOC_X","LOC_Y","SHOT_ATTEMPTED_FLAG","SHOT_MADE_FLAG"]
        self.df = self.__gen_shotchart_df()
        
    
    def __gen_shotchart_df(self,req_args=None):
        if self.type == "ZONE":
            self.columns = ["SHOT_ZONE_BASIC","SHOT_ZONE_AREA","SHOT_ZONE_RANGE",
                            "SHOT_DISTANCE","SHOT_ATTEMPTED_FLAG","SHOT_MADE_FLAG"]
        in_db = (not (self.mapping == self.raw_data == None)) and req_args == None
        if in_db:
            df = utils.genDataframeFromRawData(self.rawData,self.columns,self.mapping)
        else:
            assert req_args != None
            shotchart_req = playerShotchartRequest(query_params=req_args)
            data = shotchart_req.get_raw_data
            header_mapping = shotchart_req.get_header_mapping()
            df = utils.genDataframeFromRawData(data,self.columns,header_mapping)
        return df

    def get_zone_avgs(self):
        if self.type != "ZONE":
            return None
        
        shot_groups = self.df.groupby(by=["SHOT_ZONE_BASIC","SHOT_ZONE_AREA","SHOT_ZONE_RANGE"],as_index=False)
        shot_group_avgs = shot_groups.mean()

        shot_group_avgs.drop(columns=["SHOT_DISTANCE","SHOT_ATTEMPTED_FLAG"],inplace=True)
        shot_group_avgs.rename(columns={"SHOT_MADE_FLAG": "FG_PCT"},inplace=True)

        return shot_group_avgs
    
    def get_df(self):
        return self.df 
    

