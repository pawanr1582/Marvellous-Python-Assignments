class BankAccount:
    ROI = 10.5

    def __init__(self,a,b):
        self.Name = a
        self.Amount = b

    def Deposit(self,Amount):
        self.Amount = self.Amount + Amount

    def Withdraw(self,Amount):
        self.Amount = self.Amount - Amount

    def Calculateintrest(self):
        intrest = 0
        intrest = (self.Amount * BankAccount.ROI * 1) / 100
        return intrest
    
    def Display(self):
        print(self.Name, self.Amount, end = " ")

def main():

    BankAcc = BankAccount("Rahul", 10000)
    IntAmt = BankAcc.Calculateintrest()

    print("Intrest amount based on amount is : ",IntAmt)

if __name__ == "__main__":
    main()

