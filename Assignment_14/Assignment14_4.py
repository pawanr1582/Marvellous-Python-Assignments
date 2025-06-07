class Student:

    school_name = "School"

    def __init__(self,name,rollNo):
        self.Name = name
        self.Rollno = rollNo

    def Display(self):
        print("Name of student is : ",self.Name)
        print("Rollno of student is : ",self.Rollno)
        print("Name of School is : ",Student.school_name)

def main():

    obj = Student("Pawan",101)

    print("Initially")
    obj.Display()
    Student.school_name = "New School"
    print("After changing class name : ")
    obj.Display()

if __name__ == "__main__":
    main()


