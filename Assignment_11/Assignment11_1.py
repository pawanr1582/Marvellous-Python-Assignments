def Display(no):
    if no == 0:
        return
    Display(no-1)
    print(no,end=" ")

def main():
    print("Enter print value : ")
    no = int(input())

    Display(no)

if __name__=="__main__":
    main()