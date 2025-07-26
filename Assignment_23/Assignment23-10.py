import pandas as pd
import DataFrameModule

def DataDescription():

    df = DataFrameModule.getDataFrame()
    df.drop(columns = ["English"], inplace = True)
    print("Drop Column English")
    print(df.head())
    

def main():

    DataDescription()


if __name__ == "__main__":
    main()