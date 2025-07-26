import pandas as pd

    
def main():

    data = {"Name" : ["A", "B", "C"], "Age" : [21.0, 22.0, 23.0]}

    df = pd.DataFrame(data)

    print("Datatype of Age :")
    print(df["Age"].dtype)

    print("Data after data type change of Age col as int :")
    df["Age"] = df["Age"].astype(int)

    print(df)
    
if __name__ == "__main__":
    main()