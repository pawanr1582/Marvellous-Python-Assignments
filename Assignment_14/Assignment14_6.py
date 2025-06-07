class Calculator:

    def Addition(self,a,b):
        res = 0
        res = a+b
        return res
    
    def Substraction(self,a,b):
        res = 0
        res = a-b
        return res
    
    def Multiplication(self,a,b):
        res = 0
        res = a*b
        return res
    
    def Division(self,a,b):
        res = 0
        res = a/b
        return res

def main():

    print("Enter 2 values for arithmatic calculation : ")

    x = int(input())
    y = int(input())

    obj = Calculator()

    sum = obj.Addition(x,y)
    print("Addition of",x,"+",y,"=",sum,end=" ")

    sub = obj.Substraction(x,y)
    print("Substraction of",x,"-",y,"=",sub,end=" ")

    mul = obj.Multiplication(x,y)
    print("Multiplication of",x,"*",y,"=",mul,end=" ")

    div = obj.Division(x,y)
    print("Division of",x,"+",y,"/",div,end=" ")

if __name__ == "__main__":
    main()