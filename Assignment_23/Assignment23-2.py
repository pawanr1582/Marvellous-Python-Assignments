import pandas as pd
import DataFrameModule

def dataDescription():

    df = DataFrameModule.getDataFrame()

    print("Data Describe is as follows :")
    print(df.describe())

def main():

    dataDescription()


if __name__ == "__main__":
    main()