def minimum(inputdata):
    min = inputdata[0]

    for no in range(len(inputdata)):
        if(inputdata[no] < min):
            min = inputdata[no]

    return min

def main():
    print("Enter the number : ")
    size = int(input())

    data = []

    print("Enter numeric valuse ; ")
    for x in range(size):
        ele = int(input())
        data.append(ele)

    print(data)

    res = minimum(data)

    print("Minimum number in the list is : ",res)


if __name__=="__main__":
    main()


