import multiprocessing
import threading
import time

def Addition():
    result = 0
    for x in range (0,10000000):
        result = result + x
    #
    print("Addition is",result)
 
def main():
    start_time = time.time()
    result = Addition()
    end_time = time.time()
    print("Execution time for normal function",end_time-start_time)

    thread_start_time = time.time()
    A1 = threading.Thread(target=Addition)
    A1.start()
    A1.join()
    thread_end_time = time.time()
    print("Execution time for thread",thread_end_time-start_time)

    multiprocess_start_time = time.time()
    B1 = multiprocessing.Process(target=Addition)
    B1.start()
    B1.join()
    multiprocess_end_time = time.time()
    print("Execution time for multiprocessing",multiprocess_end_time-start_time)

if __name__ == "__main__":
    main()
