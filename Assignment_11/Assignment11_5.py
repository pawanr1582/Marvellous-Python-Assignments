counter = 0

def count(no):
    global counter
    if (no > 0):
       y = no % 10
       if(y == 0):
            counter = counter + 1
       no = no // 10
       count(no)
    return counter

def main():
    print("Enter the number to count Zero : ")
    no = int(input())
    ret = count(no)
    print("Number is : ",ret)

if __name__=="__main__":
    main()