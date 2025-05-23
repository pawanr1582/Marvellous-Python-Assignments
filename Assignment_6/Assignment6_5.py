def prime():
    
    print("Enter the number : ")
    no = int(input())

    ans = "It is prime number"
    i = 2
    while (i < no):
        if(no % i == 0):
            ans = "It is not prime number"
            break
        i = i+1

    print(ans)

if __name__=="__main__":
    prime()