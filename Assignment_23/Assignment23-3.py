import pandas as pd
import DataFrameModule

def addTotalCol():

    df = DataFrameModule.getDataFrame()

    print("Add total column in dataframe :")
    df["Total"] = df["Math"] + df["Science"] + df["English"]

    print(df.head())

def main():

    addTotalCol()


if __name__ == "__main__":
    main()