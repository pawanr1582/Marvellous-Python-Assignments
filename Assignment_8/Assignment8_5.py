import threading
import os

def Inorder():
    for x in range(1,51):
        print(x,end = " ")
        print("\n")

def Inreverse():
    for x in range(50,0,-1):
        print(x,end = " ")
        print("\n")

def main():

    thread1 = threading.Thread(target=Inorder, args=())
    thread2 = threading.Thread(target=Inreverse, args=())

    thread1.start()
    thread1.join()
    
    thread2.start()
    thread2.join()

if __name__=="__main__":
    main()
