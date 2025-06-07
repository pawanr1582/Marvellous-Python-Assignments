class Person:
    def __init__(self,name,age):
        self.Name = name
        self.Age = age

class Teacher(Person):

    def __init__(self,sub,sal,name,age):
        self.Sub = sub
        self.Sal = sal
        super().__init__(name,age)

    def Display(self):
        print("Name",self.Name)
        print("Age",self.Age)
        print("Subject",self.Sub)
        print("Salary",self.Sal)

def main():

    obj = Teacher("Mathmatics",10000,"Pawan",30)

    obj.Display()

if __name__ == "__main__":
    main()    
