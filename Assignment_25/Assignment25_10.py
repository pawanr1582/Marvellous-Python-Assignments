import pandas as pd
from sklearn.model_selection import train_test_split
    
def main():

    data = {
        "Salary" : [50000, 60000, 80000, 65000, 45000],
        "Age" : [25,30,45,35,22],
        "Purchased" : [1,0,1,0,1,]
        }
    df = pd.DataFrame(data)

    x = df.drop("Purchased", axis = 1)
    y = df["Purchased"]

    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2, random_state = 42)

    print("X Train data:")
    print(x_train)
    print("X Test data:")
    print(x_test)
    print("Y Train data:")
    print(y_train)
    print("Y Test data:")
    print(y_test)
 
       
if __name__ == "__main__":
    main()