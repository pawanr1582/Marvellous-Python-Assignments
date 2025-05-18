def len():

    print("Enter the number : ")
    x = int(input())

    count = 0
    while(x > 0):
        count = count+1
        x = x//10
    print("The len of numner is : ",count)
                

if __name__=="__main__":
    len()