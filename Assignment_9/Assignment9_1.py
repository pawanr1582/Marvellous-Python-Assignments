import threading
import time

def display():
    for x in range(1,6):
        print(x,end = " ")
        print("\n")

def main():

    A1 = threading.Thread(target=display)
    A2 = threading.Thread(target=display)
    A3 = threading.Thread(target=display)

    A1.start()
    time.sleep(1)
    A2.start()
    time.sleep(1)
    A3.start()

    A1.join()
    A2.join()
    A3.join()

if __name__=="__main__":
    main()
