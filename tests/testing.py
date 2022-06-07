import matplotlib 
import requests as req
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb



print(matplotlib.get_backend())

def make_get_request(endpoint,params):
    response = req.get(f"{HOST}{endpoint}",params=params)
    return response






if __name__ == "__main__":
    HOST="http://localhost:5000"
    params = {"shotchart_type": "HEX"}
    # endpoint = "/api/player/101108"
    endpoint = "/api/shotchart/player/1629029"
    response = make_get_request(endpoint=endpoint,params=params)
    

    if response.status_code == 200:
        # print(response.json())
        fig, ax = plt.subplots()
        x = [shot['LOC_X'] for shot in response.json()['data']]
        y = [shot['LOC_Y'] for shot in response.json()['data']]
        df = pd.DataFrame(data={'x': x,'y':y})
        # ax.scatter(x=x,y=y)
        jointgrid = sb.jointplot(x='x',y='y',data=df,kind='hex')

        
        plt.show()
        
        # import matplotlib.rcsetup as rcsetup
        # print(rcsetup.all_backends)
        # import matplotlib
        # print(matplotlib.matplotlib_fname())
