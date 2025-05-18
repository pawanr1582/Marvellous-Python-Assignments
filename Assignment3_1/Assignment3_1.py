def list(inputdata):
    sum = 0
    for no in range(len(inputdata)):
        sum = sum + inputdata[no]

    return sum

def main():
    print("Enter the number : ")
    size = int(input())

    data = []

    print("ENter numeric valuse ; ")
    for x in range(size):
        ele = int(input())
        data.append(ele)

    print(data)

    res = list(data)

    print("Addition of all number in list is : ",res)


if __name__=="__main__":
    main()


