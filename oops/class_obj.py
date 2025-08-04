# class Car:
#     brand = None
#     model = None

# my_car = Car()
# print(my_car)
# The `__init__` method in Python is a special method that is called when a new object of a
    # class is created. It is also known as the constructor method. In the context of the `Car`
    # class you provided, the `__init__` method initializes the attributes `brand` and `model` of
    # the `Car` object with the values passed as arguments when creating a new instance of the
    # `Car` class.

class Car:
    total_cars = 0
    def __init__(self, brand, model):
        self.__brand = brand  # Make it private to access through method
        self.model = model
        Car.total_cars += 1

    def get_brand(self):
        return self.__brand + "!!!"
        
    def full_name(self):
        return f"{self.get_brand()} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
       

my_Car = Car("Toyota", "Corolla")
print(my_Car.get_brand())     # ✅ Correct way to call the method
print(my_Car.model)

my_new_car = Car("TATA", "SAFARI")
print(my_new_car.get_brand())
print(my_new_car.model)
print(my_new_car.full_name())

# Inheritance
# In inheritance, a child class inherits the attributes and methods of a parent class.
# Here car is the parent class and ElectricCar is the child class
# This child class inherits the attributes and methods of the parent class
# ALong with adding new attributes and methods like `battery_size`
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Battery--> electric charge"    

my_tesla = ElectricCar("Tesla", "Model S", "21kWh")

print(my_tesla.get_brand())         # ✅ Now works
print(my_tesla.full_name())         # ✅ Inherited method
print(my_tesla.fuel_type())


# Polymorphism
# Polymorphism is the ability of objects to take on multiple forms.


