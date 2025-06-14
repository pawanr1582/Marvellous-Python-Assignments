import os
def main():

    print("Enter the file name : ")
    fileName = input()

    flag = os.path.exists(fileName)

    if(flag == False):
        print("Enter valid file name")
        exit()

    fobj1 = open("Destination.txt","w")
    fobj = open(fileName,"r")

    sourcefileData = fobj.read()

    fobj1.write(sourcefileData)
        
    fobj.close()
    fobj1.close()
    
if __name__ == "__main__":
    main()