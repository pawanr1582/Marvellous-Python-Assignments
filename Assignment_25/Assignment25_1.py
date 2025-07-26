import numpy as np

def Outlier_detection_IQR(data):

    
    Q1 = np.percentile(data,25)
    Q3 = np.percentile(data,75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = []

    for x in data :
        if(x < lower_bound or upper_bound < x):
            outliers.append(x)
    return outliers,lower_bound,upper_bound


def main():

    data = {"Salary" : [25000, 27000, 29000, 31000, 50000, 100000]}

    sal_data = data["Salary"]
    outliers, lower, upper = Outlier_detection_IQR(sal_data)

    print(f"Lower Bounnd : {lower}")
    print(f"Upper Bounnd : {upper}")
    print(f"Detected Outliers : {outliers}")

    
if __name__ == "__main__":
    main()