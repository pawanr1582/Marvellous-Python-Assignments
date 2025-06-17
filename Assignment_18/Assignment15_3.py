import os
import sys
def main():

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This program is use for copying data from another file.")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Used the given Script as")
            print("ScriptName.py Argument1")
        else:
            fileName = sys.argv[1]
            flag = os.path.exists(fileName)
            if(flag == False):
                print("Enter valid name of the file name to write data to Demo.txt file")
                exit()

            fobj = open("Demo.txt","w")

            fobj2 = open(sys.argv[1],"r")
            data = fobj2.read()

            fobj.write(data)

            fobj.close()
            fobj2.close()

    else:
        print("Invalid number of arguments")
        print("Used the given flag as : ")
        print("--h : Used to display the help.")
        print("--u : Used to display the usage.")
            

if __name__ == "__main__":
    main()
