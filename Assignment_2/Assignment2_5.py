def num(no):
    i = 2
    while i < no:
        if(no%i== 0):
            print("It isnot Prime number")
            break
        i = i + 1
    print("It is Prime number")

def main():
    print("Enter the number : ")
    no = int(input())

    result = num(no)
    print("Factorial number is : ",result)

if __name__=="__main__":
    main()

