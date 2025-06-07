class Employee:

    def __init__(self,name,id,salary):
        self.Name = name
        self.ID = id
        self.Salary = salary

    def Display(self):
        print("Name",self.Name)
        print("ID",self.ID)
        print("Salary",self.Salary)

def main():
    obj = Employee("Rohit",101,5000)
    obj.Display()

if __name__ == "__main__":
    main()