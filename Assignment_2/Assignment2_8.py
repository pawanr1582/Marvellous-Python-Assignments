def num():

    print("Enter the pattern number : ")
    size = int(input())+2

    for x in range(1,size):
        for j in range(1,x):
            print(j,end=" ")
        print("\n")
                

if __name__=="__main__":
    num()