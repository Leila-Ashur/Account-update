 
#  
# 2) Create 3 files in the classes directory car.py, fruit.py, and bank.py.
# Define the following classes in each module respectively. 
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.
class Car:
    brand = "Subaru"
    
    def __init__(self, model, color,fuel_type):
        self.model = model
        self.color = color
        self.year_made = fuel
        
    def start(self):
        print(f"The {self.color} {self.model} is from the fuel station to be {self.fuel}")
    
    
    def accelerate(self):
       
        print(f"The {self.color}  {self.model} is now going in high speed after adding more{self.fuel}.")
    
    def stop(self):
       
        print(f"The {self.color} {self.model} has stop moving due to no {self.fuel}.")
        
