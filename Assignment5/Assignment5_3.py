def vote():

    print("Enter your age : ")

    age = int(input())

    if(age >= 18):
        print("Eligible for voting")
    else:
        print("not Eligible for voting")
    
if __name__=="__main__":
    vote()
