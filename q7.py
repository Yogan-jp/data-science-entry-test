#Task1 
class Car:
    def __init__(self, make, model, year): # __init__ method is declared within a class and is used to initialize the attributes of an object as soon as the object is formed
        self.make = make # represents the instance of class
        self.model = model  # represents the instance of class
        self.year = year # represents the instance of class
    def describe_car(self): 
        print(f"{self.year} {self.make} {self.model}") # Print a description of the car
#Task2
# Creating an instance of the Car class with specific attributes
my_car = Car("Toyota", "Corolla", 2020)
# Calling the describe_car method to print the formatted string
my_car.describe_car() # Expected result will be "2020 Toyota Corolla"
