sqr = lambda a : a*a
cube = lambda b : b**3

def main():

    print("Enter the number")
    no = int(input())

    res = sqr(no)
    print("Square of ",no , "is :",res)

    res = cube(no)
    print("Cube of",no , "is :",res)

if __name__=="__main__":
    main()
