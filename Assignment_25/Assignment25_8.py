import pandas as pd
import numpy as np
    
def main():

    data = {"Marks" : [85,np.nan,90,np.nan,95]}
    df = pd.DataFrame(data)

    print("Original Dataframe : ")

    print(df)

    df_interpolated = df.interpolate()

    print("\nDataFrame after linear interpolation : ")
    print(df_interpolated)
    
       
if __name__ == "__main__":
    main()