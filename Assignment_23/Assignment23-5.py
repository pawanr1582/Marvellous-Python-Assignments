import pandas as pd
import DataFrameModule

def ChangeNameValue():

    df = DataFrameModule.getDataFrame()

    print(df.head())
    print("Get updated data :")

    df["Name"].replace("Pooja","Puja", inplace = True)
    print(df.head())
    

def main():

    ChangeNameValue()


if __name__ == "__main__":
    main()