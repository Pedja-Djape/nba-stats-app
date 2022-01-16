import pandas as pd 

def genDataframeFromRawData(rawData,columns,mapping):
    # Raw data is list of lists
    transformData = [
        tuple(dataPoint[mapping[column]] for column in columns)
        for dataPoint in rawData
    ]
    data = pd.DataFrame.from_records(transformData,columns=columns)
    return data

