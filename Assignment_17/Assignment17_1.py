import schedule
import time

def Display():
    print("Time schedular.....")

def main():

    print("Inside automation script")
    schedule.every(2).seconds.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

