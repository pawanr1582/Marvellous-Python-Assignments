import pandas as pd

def getDataFrame():

    data = {
    "Name" : ["Amit", "Sagar", "Pooja"],
    "Math" : [85,90,78],
    "Science" : [92,88,80],
    "English" : [75,85,82],
    }

    df = pd.DataFrame(data)

    return df