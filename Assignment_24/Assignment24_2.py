import pandas as pd
import Dataframemodule

def main():

    df = Dataframemodule.getDataFrame()

    df.insert(4,"Gender",["Male", "Male", "Female"])
    print("Data befor Encoding : ")
    print(df)

    df["Gender"] = df["Gender"].map({"Female":0, "Male":1})
    print("Data after Encoding : ")
    print(df)


if __name__ == "__main__":
    main()