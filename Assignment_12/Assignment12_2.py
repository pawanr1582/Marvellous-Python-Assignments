class Circle:
    PI = 3.14
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.circumferance = 0.0

    def Accept(self,r):
        self.Radius = r
    
    def calculateArea(self):
        self.Area = self.Radius * self.Radius * Circle.PI
    
    def calculateCircumferance(self):
        self.circumferance = 2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius of Circle is : ",self.Radius)
        print("Area of Circle is : ",self.Area)
        print("Area of Circumferance is : ",self.circumferance)

def main():

    print("Enter radius of CIrcle : ")
    a = int(input())

    cir = Circle()
    cir.Accept(a)
    cir.calculateArea()
    cir.calculateCircumferance()
    cir.Display()

    print("Enter radius of CIrcle : ")
    b = int(input())

    cir = Circle()
    cir.Accept(b)
    cir.calculateArea()
    cir.calculateCircumferance()
    cir.Display()


if __name__ == "__main__":
    main()