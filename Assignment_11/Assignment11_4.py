PowerNum = 1

def power(no,p):
    global PowerNum
    if (p > 0):
       PowerNum = PowerNum * no
       p = p-1
       power(no,p)
    return PowerNum

def main():
    print("Enter number : ")
    no = int(input())
    print("Enter raise to number : ")
    raiseNum = int(input())
    ret = power(no,raiseNum)
    print("Number is : ",ret)

if __name__=="__main__":
    main()