import os
def main():

    print("Enter name of file : ")
    fileName = input()

    flag = os.path.exists(fileName)
    if(flag == False):
        print("Please enter the valid file name")
        exit()

    fobj = open(fileName,"r")
    data = fobj.read()
    print("File contents are as follow : ")
    print(data)

    fobj.close()
    
if __name__ == "__main__":
    main()