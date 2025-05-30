import threading
import os

def capitalCount(inputData):
    counter = 0
    print("PID os capitalCount is : ",os.getpid())
    print("This tread name is", threading.current_thread().name)

    for x in range(len(inputData)):
        if(inputData[x].isupper() == True):
            counter = counter + 1
        print("Number of capital letter are : ",counter)

def smallCount(inputData):
    counter = 0
    print("PID os capitalCount is : ",os.getpid())
    print("This tread name is", threading.current_thread().name)

    for x in range(len(inputData)):
        if(inputData[x].islower() == True):
            counter = counter + 1
        print("Number of small letter are : ",counter)

def digitCount(inputData):
    counter = 0
    print("PID os capitalCount is : ",os.getpid())
    print("This tread name is", threading.current_thread().name)

    for x in range(len(inputData)):
        if(inputData[x].isdigit() == True):
            counter = counter + 1
        print("Number of small letter are : ",counter)

def main():

    print("Enter size of elements:")
    num = int(input())

    print("Enter the numeric values")

    data = []
    for i in range(num):
        data.append(input())

    capital = threading.Thread(target=capitalCount, args=(data,))
    small = threading.Thread(target=smallCount, args=(data,))
    digit = threading.Thread(target=digitCount, args=(data,))

    capital.start()
    small.start()
    digit.start()

    capital.join()
    small.join()
    digit.join()

if __name__=="__main__":
    main()





    

