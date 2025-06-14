import os
def main():

    print("Enter the file name : ")
    fileName = input()

    flag = os.path.exists(fileName)

    if(flag == False):
        print("Enter valid file name")
        exit()

    fobj = open(fileName,"r")
    fobj1 = open("New.txt","w")

    lines = fobj.readlines()

    for line in lines:
        if line.strip() == "":
            continue
        else:
            fobj1.write(line)


    fobj.close()
    fobj1.close()
   
    
if __name__ == "__main__":
    main()