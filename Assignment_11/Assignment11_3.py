Sum = 0
def SUM_OF_DIGIT(no):
    global Sum
    if (no > 0):
       y = no%10              # Reminder of Division
       Sum = Sum + y
       no = no // 10          # Quetiont
       SUM_OF_DIGIT(no)
    return Sum

def main():
    print("Enter number for digit addition : ")
    no = int(input())
    ret = SUM_OF_DIGIT(no)
    print("Addition is : ",ret)

if __name__=="__main__":
    main()