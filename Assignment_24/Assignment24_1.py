import pandas as pd
import Dataframemodule

def main():

    df = Dataframemodule.getDataFrame()

    df["normalized_value"] = (df["Math"] - df["Math"].min()) / (df["Math"].max() - df["Math"].min())
    print(df["normalized_value"])


if __name__ == "__main__":
    main()