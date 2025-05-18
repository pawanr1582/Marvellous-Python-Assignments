from functools import reduce

def prime(val):
    ans = True
    i=2
    while (i < val):
        if(val % i == 0):
            ans = False
            break
        i = i+1

    if(ans == True):
        return ans
    
def multiplication(val):
        mult = val * 2
        return mult
    
def maxNumber(val1, val2):
        if(val1 < val2):
            return val2
        else:
            return val1


def main():
    print("Enter size of elements : ")
    size = int(input())

    inputdata = []

    for i in range(size):
        inputdata.append(int(input()))

    Fdata = list(filter(prime,inputdata))
    print("Filer data is :",Fdata)

    Mdata = list(map(multiplication,Fdata))
    print("Map data is :",Mdata)

    Rdata = reduce(maxNumber,Mdata)
    print("Reduce data is :",Rdata)

if __name__=="__main__":
    main()