import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import Dataframemodule


def main():

    df = Dataframemodule.getDataFrame()
    df.insert(4,"Total",df["Math"]+df["Science"]+df["English"])

    conditional_series = np.where(df["Total"] >= 250, "Pass", "Fail")
    df.insert(5, "Status",conditional_series)

    x = df["Name"]
    y = df["Math"]
    
    plt.hist(df["Math"], bins = 100, color = "skyblue", edgecolor = "black")

    plt.title("Marks of Maths")
    plt.xlabel("Maths Mark")
    plt.ylabel("Frequency")
    
    
    plt.show()

if __name__ == "__main__":
    main()