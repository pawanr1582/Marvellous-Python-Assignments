def riTrangle(no, counter):
   
    if (counter < no):
         for x in range(counter):
             print("*",end=" ")
         print("\n")
         counter = counter + 1
         riTrangle(no,counter)

def main():
    riTrangle(5,1)

if __name__=="__main__":
    main()