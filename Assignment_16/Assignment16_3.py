import os
def main():

    print("Enter name of file to count the line, words and count : ")
    fileName = input()

    flag = os.path.exists(fileName)
    if(flag == False):
        print("Please enter the valid file name")
        exit()

    fobj = open(fileName,"r")
    
    lineCount = 0
    wordCount = 0
    characters = 0

    lines = fobj.readlines()

    for line in lines:
        lineCount = lineCount + 1
        for word in line.split():
            wordCount = wordCount + 1
            for i in word:
                characters = characters + 1
                
    fobj.close()

    print("Number of lines are : ",lineCount)
    print("Number of words are : ",wordCount)
    print("Number of Characters are : ",characters)
    
if __name__ == "__main__":
    main()