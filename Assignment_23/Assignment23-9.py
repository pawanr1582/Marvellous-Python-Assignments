import pandas as pd
import numpy as np

def GetMaxScoreInSci():

    data = {
        "Name" : ["Amit", "Sagar", "Pooja"],
        "Math" : [np.nan,78,90],
        "English" : [75,np.nan,82],
    }
    

    df = pd.DataFrame(data)
    print(df)
    df.fillna(df.mean(numeric_only = True),inplace=True)
    print(df)
    

def main():

    GetMaxScoreInSci()


if __name__ == "__main__":
    main()