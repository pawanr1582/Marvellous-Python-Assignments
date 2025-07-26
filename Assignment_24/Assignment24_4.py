import pandas as pd
import Dataframemodule
import matplotlib.pyplot as plt

def main():

    df = Dataframemodule.getDataFrame()

    subject = ["Math", "Science", "English"]
    marks = df[df["Name"] == "Sagar"] [["Math", "Science", "English"]].values.flatten()

    plt.pie(marks, labels=subject)

    plt.title("Marks of Sagar")
    plt.axis("equal")
    plt.show()
    
if __name__ == "__main__":
    main()