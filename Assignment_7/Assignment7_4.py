from functools import reduce

def main():

    print("Enter the number")
    no = int(input())

    print("Enter numeric values : ")
    data = []
    for i in range(no):
        data.append(int(input()))

    Rdata = reduce(lambda a,b : a*b, data)
    print("Reduce data is : ")
    print(Rdata)

if __name__=="__main__":
    main()
