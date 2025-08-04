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

class Car :
     
    def __init__(self , brand , model):
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand} {self.model} "
       



my_Car = Car("Toyota" , "Corola")
print(my_Car.brand)    
print(my_Car.model) 


my_new_car = Car("TATA" , "SAFARI")
print(my_new_car.brand)
print(my_new_car.model)
print(my_new_car.full_name())



#Inheritance --> Inherit from the parent class 
class ElectricCar (Car) :
    def __init__(self, brand, model , battery_size):
        super().__init__(brand, model )
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla" , "Model s" , "21kwh")

print(my_tesla.brand)