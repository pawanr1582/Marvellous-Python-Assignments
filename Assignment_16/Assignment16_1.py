import sys
def main():

    fobj = open("Student.txt","w")
    print("Enter name of 5 students : ")
    
    for x in range(5):
        fobj.write(input())
        fobj.write("\n")
    
    fobj.close()

if __name__ == "__main__":
    main()