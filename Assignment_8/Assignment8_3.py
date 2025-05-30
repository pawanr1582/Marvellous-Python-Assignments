import threading

def evenAdd(no):
    sum = 0
    for x in range(len(no)):
        if(no[x] % 2 == 0):
            sum = sum + no[x]
    print("Addition of even number is", sum)

def oddAdd(no):
    sum = 0
    for x in range(len(no)):
        if(no[x] % 2 !=0):
            sum = sum + no[x]
    print("Addition of odd number is", sum)

def main():

    print("Enter number : ")
    num = int(input())

    print("Enter the numberic values")

    data = []
    for i in range(num):
        data.append(int(input()))

    evenlist = threading.Thread(target=evenAdd, args=(data,))
    oddlist = threading.Thread(target=oddAdd, args=(data,))

    evenlist.start()
    oddlist.start()

    evenlist.join()
    oddlist.join()

    print("Exit from main")

if __name__=="__main__":
    main()
