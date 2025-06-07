class Employee:

    def __init__(self,name,salary,dept):
        self.Name = name
        self.Salary = salary
        self.Dept = dept

    def Display(self):
        print("Name:",self.Name)
        print("Salary:",self.Salary)
        print("Dept:",self.Dept)

def main():

    obj = Employee("Pawan",10000,"HR")
    obj.Display()

    print(obj.Name)
    print(obj.Dept)

if __name__ == "__main__":
    main()