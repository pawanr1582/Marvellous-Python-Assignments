def temp():
    print("Enter trmperature in celsius :")
    temp = int(input())

    F = (temp * (9/5)) + 32

    print("Temperature in Fahrenhiet : ",F)

if __name__=="__main__":
    temp()

