import schedule
import datetime
import time

def CurrentTime():

    fobj = open("Marvellous.txt","a")
    CurrentTime = str(datetime.datetime.now())
    fobj.write(CurrentTime)
    fobj.write("/n")
    
    fobj.close()

def main():

    schedule.every(2).minutes.do(CurrentTime)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

