import pandas as pd
import matplotlib.pyplot as plt
import Dataframemodule

def main():

    df = Dataframemodule.getDataFrame()
    
    x = df["English"]

    plt.boxplot(x)
    plt.title("Box Plot of English mark data distribution and outliers")
    plt.ylabel("Value")
    plt.show()


if __name__ == "__main__":
    main()