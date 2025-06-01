mul = lambda a,b : a*b

def main():
    print("Enter first number :")
    no1 = int(input())

    print("Enter second number")
    no2 = int(input())

    result = mul(no1,no2)

    print("Multiplication is : ",result)

if __name__=="__main__":
    main()