import schedule
import time

def Backup():

    fobj = open("Logfile.txt","a")
    fobj.write("Taking backup...\n")
        
    fobj.close()

def main():

    schedule.every(1).minutes.do(Backup)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

