import os
def main():

    print("Enter the file name : ")
    fileName = input()

    flag = os.path.exists(fileName)

    if(flag == False):
        print("Enter valid file name")
        exit()

    fobj = open(fileName,"r")
    lines = fobj.readlines()

    for line in lines:
        for word in line.split():
            if(word.isnumeric() == False):
                nameofstudent = word
            if(word.isnumeric() == True and int(word) > 75):
                print(nameofstudent)
    
    fobj.close()
   
    
if __name__ == "__main__":
    main()