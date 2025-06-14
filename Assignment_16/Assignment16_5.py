import os
def main():

    print("Enter the file name to display lines having more than 5 words: ")
    fileName = input()

    flag = os.path.exists(fileName)
    if(flag == False):
        print("Enter valid file name")
        exit()

    fobj = open(fileName,"r")

    counter = 0

    linesInfile = fobj.readlines()

    for x in linesInfile:
        counter = 0

        for word in x.split():
            counter = counter + 1
            if(counter>5):
                print(x)
                break

    
    fobj.close()
    
if __name__ == "__main__":
    main()