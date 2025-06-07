class number:
    def __init__(self,a):
        self.value = a

    def chkPrime(self):

        ans = True
        i = 2
        while (i < self.value):
            if(self.value % i == 0):
                ans = False
                break
            i = i + 1
        if(ans == True):
            return "Prime Number"
        else:
            return "Not Prime number"
        
    def checkPerfect(self):
        sum = self.sumfactor()
        if(sum == self.value):
            return "Perfect Number"
        else:
            return "Not Perfect Number"
    
    def sumfactor(self):
        sum = 0
        i = 1
        while(i < self.value):
            if(self.value % i == 0):
                sum = sum + 1
            i = i + 1
        return sum
    
    def factor(self):
        factorlist = []
        i = 1
        while(i < self.value):
            if(self.value % 1 == 0):
                factorlist.append(1)
            i = i+1
        return factorlist

def main():

    print("Enter the number")
    a = int(input())

    obj1 = number(a)
    ret = obj1.chkPrime()
    print(a, "is", ret, end = " ")
    print("\n")

    ret = obj1.checkPerfect()
    print(a, "is", ret, end = " ")
    print("\n")

    ret = obj1.sumfactor()
    print("Sum of factor is : ",ret, end = " ")

    ret = obj1.factor()
    print("factor list is : ",ret, end = " ")
    print("\n")

if __name__ == "__main__":
    main()

