class Vehicle:

    def start(self):
        print("In base class method")

class Car:

    def start(self):
        print("In drive class start")

def main():

    obj = Car()

    obj.start()

if __name__ == "__main__":
    main()