rev = lambda x : x == reversed(x)

def main():

    print("Enter your number : ")
    inputstr = input()

    res = rev(inputstr)

    if(res):
        print(inputstr,"is palimdrom")
    else:
        print(inputstr,"is not palimdrom")
    
if __name__=="__main__":
    main()
