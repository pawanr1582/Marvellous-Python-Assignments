import pandas as pd
import DataFrameModule

def SortTotalMarks():

    df = DataFrameModule.getDataFrame()

    print("Get Sorted data :")

    df.insert(4, "Total", df["Math"] + df["Science"] + df["English"])

    sorted_df = df.sort_values(by=["Total"], ascending=False)
    print(sorted_df)
    

def main():

    SortTotalMarks()


if __name__ == "__main__":
    main()