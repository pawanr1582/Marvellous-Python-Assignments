import schedule
import time
import datetime

def Displaycurrenttime():
    print(datetime.datetime.now())

def main():

    print("Inside automation script")
    schedule.every(1).minutes.do(Displaycurrenttime)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

