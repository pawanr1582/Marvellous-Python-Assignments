def sum():

    print("Enter the number : ")
    x = int(input())

    count = 0
    while(x > 0):
        count = count+(x % 10)
        x = x//10
    print("The sum of numner is : ",count)
                

if __name__=="__main__":
    sum()