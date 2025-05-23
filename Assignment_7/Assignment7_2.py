doub = lambda a : a*2

def main():

    print("Enter the number : ")
    no = int(input())

    print("Enter numeric values : ")
    data = []
    for i in range(no):
        data.append(int(input()))

    Mdata = list(map(doub,data))
    print("Map data is : ")
    print(Mdata)

if __name__=="__main__":
    main()
