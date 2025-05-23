def main():

    print("Enter alphbet : ")
    no1 = input()

    print("-----------")

    if(no1 == "a" or no1 == "e" or no1 == "i" or no1 == "o" or no1 == "u"):
        print(no1, "is vowel")
    else:
        print(no1, "is consonant")
    
if __name__=="__main__":
    main()
