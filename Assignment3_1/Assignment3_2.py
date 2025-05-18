def maximum(inputdata):
    max = 0

    for no in range(len(inputdata)):
        if(inputdata[no] > max):
            max = inputdata[no]

    return max

def main():
    print("Enter the number : ")
    size = int(input())

    data = []

    print("ENter numeric valuse ; ")
    for x in range(size):
        ele = int(input())
        data.append(ele)

    print(data)

    res = maximum(data)

    print("Maximum number in the list is : ",res)


if __name__=="__main__":
    main()


