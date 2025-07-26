import pandas as pd
import DataFrameModule

def dataframeInfo():

    df = DataFrameModule.getDataFrame()

    print("Basic information of Data")
    print("Dimention of data is :",df.shape)
    print("Columns name is :", df.columns)
    print("Datatype of columns are :")
    print(df["Name"].dtype)
    print(df["Math"].dtype)
    print(df["Science"].dtype)
    print(df["English"].dtype)

def main():

    dataframeInfo()


if __name__ == "__main__":
    main()