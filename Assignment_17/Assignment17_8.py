import schedule
import time

def mailinboxupdatechk():

    print("Cheking mail.....")

def main():

    schedule.every(10).seconds.do(mailinboxupdatechk)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

