class BankAccount:

    def __init__(self,accountNum,name,balance):
        self.AccNo = accountNum
        self.Name = name
        self.Bal = balance

    def Deposite(self,amount):
        self.Bal = self.Bal + amount
        return self.Bal
    
    def Withdrawl(self,amount):
        if(amount > self.Bal):
            print("No sufficiant Balance for withdrawl")
        else:
            self.Bal = self.Bal - amount
        
        return self.Bal
    
    def Display(self):
        print("Account Number",self.AccNo)
        print("Name",self.Name)
        print("Account Balance",self.Bal)

def main():

    obj = BankAccount(123,"Pawan",5000)

    print("Initial Balance : ")
    obj.Display()

    obj.Deposite(1000)
    print("After amount deposite : ")
    obj.Display()

    obj.Withdrawl(3000)

    obj.Withdrawl(1000)
    print("After amount withdrawal")
    obj.Display()

if __name__=="__main__":
    main()

