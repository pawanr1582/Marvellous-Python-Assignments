import Marvellousnum

def listprime(inputdata):
    sum = 0

    for no in range(len(inputdata)):
        ans = Marvellousnum.chkprime(inputdata[no])
        if(ans == True):
            sum = sum+inputdata[no]

    return sum

def main():
    print("Enter the number : ")
    size = int(input())

    data = []

    print("Enter numeric valuse ; ")
    for x in range(size):
        ele = int(input())
        data.append(ele)

    print(data)

    res = listprime(data)

    print("Frequency of prime number : ",res)


if __name__=="__main__":
    main()


