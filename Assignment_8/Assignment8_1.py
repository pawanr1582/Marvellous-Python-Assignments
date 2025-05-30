import threading

def checkEven(no):

    for x in range(no):
        if(x % 2 ==0):
            print(x)

def checkOdd(no):
    for x in range(no):
        if(x % 2 != 0):
            print(x)

def main():
    even = threading.Thread(target = checkEven, args=(100,))
    odd = threading.Thread(target = checkOdd, args=(100,))

    print("Even number is : ")
    even.start()
    print("Odd number is : ")
    odd.start()

    even.join()
    odd.join()

if __name__=="__main__":
    main()