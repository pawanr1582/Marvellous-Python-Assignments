import pandas as pd
import numpy as np
import Dataframemodule


def main():

    df = Dataframemodule.getDataFrame()
    df.insert(4,"Total",df["Math"]+df["Science"]+df["English"])

    conditional_series = np.where(df["Total"] >= 250, "Pass", "Fail")
    df.insert(5, "Status",conditional_series)

    print(df)

    
if __name__ == "__main__":
    main()