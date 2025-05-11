def div(value1):
    
    if (value1 % 5 == 0):
        return True
   
    else:
       return False

print("Enter divisible number of 5 :")
value1 = (int(input()))

output = div(value1)
print("The number is :",output)

if __name__=="__div__":
    div(value1)