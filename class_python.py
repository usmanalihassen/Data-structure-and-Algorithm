class Car:
    # Constructor to initialize properties
    def __init__(self, brand, color):
        self.brand = brand  # Property: brand
        self.color = color  # Property: color

    # Method to describe the car
    def describe(self):
        return f"This is a {self.color} {self.brand}."

# Create objects from the Car class
car1 = Car("Toyota", "red")
car2 = Car("Tesla", "black")
car3= Car("v8","white")

print(car1.describe())  # Output: This is a red Toyota.
print(car2.describe())  # Output: This is a black Tesla.
print(car3.describe())