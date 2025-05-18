from functools import reduce

evenNum = lambda val : (val % 2 == 0)
sqrEven = lambda b : (b*b)
listAdd = lambda b,a : (b+a)

def main():
    print("Enter size of elements : ")
    size = int(input())

    inputdata = []

    for i in range(size):
        inputdata.append(int(input()))

    Fdata = list(filter(evenNum,inputdata))
    print("Filer data is :",Fdata)

    Mdata = list(map(sqrEven,Fdata))
    print("Map data is :",Mdata)

    Rdata = reduce(listAdd,Mdata)
    print("Reduce data is :",Rdata)

if __name__=="__main__":
    main()