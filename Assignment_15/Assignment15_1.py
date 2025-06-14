import os
def main():
    print("Enter file name for check is exist in current directory or not?")
    fileName = input()

    flag = os.path.exists(fileName)

    if(flag == True):
        print(fileName, "exist",end=" ")
    else:
        print(fileName,"does not exist",end=" ")

if __name__ == "__main__":
    main()