def addfact(no):
    fact = 0
    for x in range(1,no):
        if(no%x== 0):
            fact = fact + x
    return fact


def main():
    
    print("Enter the number : ")
    no = int(input())

    result = addfact(no)
    print("Factorial numner is :", result)

if __name__=="__main__":
    main()