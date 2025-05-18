def stars():
    print("Enter your number for stars : ")
    size = int(input())

    for x in range(size,0,-1):
        for j in range(x):
            print("*",end=" ")
        print("\n")

if __name__=="__main__":
    stars()