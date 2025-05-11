def Num(no1):
    
    if (no1 > 0):
        return "Positive Number"
        
    if (no1 < 0):
        return "Negative Number"
    
    if (no1 == 0):
        return "Zero Number"
    
    else:
        return "Zero"
    
print("Enter your number :")
no1 = int(input())

output = Num(no1)
print("your Output is :", output)