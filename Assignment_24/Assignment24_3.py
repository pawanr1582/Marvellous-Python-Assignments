import pandas as pd
import Dataframemodule

def main():

    df = Dataframemodule.getDataFrame()

    df.insert(4,"Gender",["Male", "Male", "Female"])
    grouped_data = df.groupby("Gender")

    for x,y in grouped_data:
        print(f"{x}\n{y}\n")

    print("Average data of groupby Values")
    avg_data = df.groupby("Gender")[["Math","Science","English"]].mean()

    print(avg_data)

if __name__ == "__main__":
    main()