from functools import reduce

greaterNum = lambda val : (70 <= val and val <= 90)
addTen = lambda b : (b+10)
listMul = lambda b,a : (b*a)

def main():
    print("ENter size of elements : ")
    size = int(input())

    inputdata = []

    for i in range(size):
        inputdata.append(int(input()))

    Fdata = list(filter(greaterNum,inputdata))
    print("Filer data is :",Fdata)

    Mdata = list(map(addTen,Fdata))
    print("Map data is :",Mdata)

    Rdata = reduce(listMul,Mdata)
    print("Reduce data is :",Rdata)

if __name__=="__main__":
    main()