def fact():
    
    print("Enter the number : ")
    no = int(input())

    fact=1
    for x in range(no,1,-1):
        fact = fact*x

    print("factorial of",no ,"is : ", fact)

if __name__=="__main__":
    fact()