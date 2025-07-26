import pandas as pd

def getDataFrame():

    data = {
    "Name" : ["Amit", "Sagar", "Pooja"],
    "Math" : [85,78,90],
    "Science" : [92,88,80],
    "English" : [75,85,82],
    }

    df = pd.DataFrame(data)

    return df