import pandas as pd
import DataFrameModule
import matplotlib.pyplot as plt

def BarDiagramforStudentsVsTotal():

    df = DataFrameModule.getDataFrame()

    print("Get Sorted data :")

    df.insert(4, "Total", df["Math"] + df["Science"] + df["English"])

    plt.bar(df["Name"], df["Total"])
    plt.xlabel("Name")
    plt.title("Student Bar Plot")
    plt.show()
    

def main():

    BarDiagramforStudentsVsTotal()


if __name__ == "__main__":
    main()