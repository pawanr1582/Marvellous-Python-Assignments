class Rectangle:

    def __init__(self,width,length):
        self.Width = width
        self.Length = length

    def Area(self):
        area = 0
        area = self.Width * self.Length
        return area
    
    def parameter(self):
        peri = 0
        peri = 2 * (self.Width + self.Length)
        return peri
    
def main ():

        obj1 = Rectangle(10,5)

        area = obj1.Area()
        print("Area of Rectangle is : ",area)

        parameter = obj1.parameter()
        print("parameter of rectangle is : ",parameter)

if __name__ == "__main__":
    main()