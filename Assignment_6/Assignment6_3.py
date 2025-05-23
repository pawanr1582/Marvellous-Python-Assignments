def table():
    
    print("Enter the number : ")
    no = int(input())

    i=1
    while(i <= 100):
        print(no, "*", i , "=",no*i)

        i=i+1
    

if __name__=="__main__":
    table()