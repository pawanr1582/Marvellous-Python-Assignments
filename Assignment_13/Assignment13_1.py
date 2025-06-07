class Bookstore:
    NoofBooks = 0

    def __init__(self,name,author):
        Bookstore.NoofBooks = Bookstore.NoofBooks + 1
        self.Name = name
        self.Author = author

    def Display(self):

        print(Bookstore.NoofBooks , ",",self.Name,"==>",self.Author,end=" ")
        print("\n")

def main():

    obj = Bookstore("Linux System Programming","Robert Love")
    obj.Display()

    obj1 = Bookstore("C Programming","Dennis Ritchie")
    obj1.Display()

if __name__ == "__main__":
    main()




