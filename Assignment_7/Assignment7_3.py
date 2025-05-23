even = lambda a : (a % 2 == 0)

def main():

    print("Enter the number")
    no = int(input())

    print("Enter numeric values : ")
    data = []
    for i in range(no):
        data.append(int(input()))

    Fdata = list(filter(even,data))
    print("Even data is : ")
    print(Fdata)

if __name__=="__main__":
    main()
