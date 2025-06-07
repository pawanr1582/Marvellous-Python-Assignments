class Product:

    def __init__(self,name,price):
        self.Name = name
        self.Price = price

    def __eq__(self,b):
        if(self.Price == b.Price):
            print(self.Name, "and",b.Name, "price are same",end=" ")
        else:
            print(self.Name, "and",b.Name, "price are not same",end=" ")
        print("\n")

def main():

    product1 = Product("LCD",10000)
    product2 = Product("Mouse",800)

    product2.__eq__(product1)

    product1 = Product("HP Laptop",20000)
    product2 = Product("KeyBoard",2000)

    product1.__eq__(product2)

if __name__ == "__main__":
    main()
        