sum = 0

def SumNum(no):
    global sum
    if (no > 0):
         sum = sum + no
         no = no - 1
         SumNum(no)
    return sum

def main():
    print("Enter the number for addition of natural number : ")
    no = int(input())
    ret = SumNum(no)
    print("Number is : ",ret)

if __name__=="__main__":
    main()