def display(no):
    for i in range(no):
        j=0
        while(j < no):
            print("*", end=" ")
            j=j+1
        print("\n")

def main():

    print("Enter the pattern number : ")
    no = int(input())

    display(no)
    

if __name__=="__main__":
    main()