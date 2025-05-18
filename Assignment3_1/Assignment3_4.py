def frequency(inputdata,num):
    no = 0

    for no in range(len(inputdata)):
        if(inputdata[no] == num):
            no = no+1

    return no

def main():
    print("Enter the number : ")
    size = int(input())

    data = []

    print("Enter numeric valuse ; ")
    for x in range(size):
        ele = int(input())
        data.append(ele)

    print(data)

    print("Number to Search : ")
    search = int(input())

    res = frequency(data,search)

    print("Minimum number in the list is : ",res)


if __name__=="__main__":
    main()


