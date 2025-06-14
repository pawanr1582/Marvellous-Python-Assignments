import os
def main():
    print("Enter the file which you want to read")
    fileName = input()

    flag = os.path.exists(fileName)

    if(flag == False):
        print("Please enter valid name of file")
        exit()

    fobj = open(fileName,"r")
    data = fobj.read()

    print("File contains are as follow")
    print(data)

    fobj.close()

if __name__ == "__main__":
    main()
