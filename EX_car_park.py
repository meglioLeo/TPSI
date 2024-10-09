from datetime import datetime    #import to get the function to obtain the current date

class Car:

    car_count = 0   #counter that keeps track of the number of cars

    def __init__(self, model, make, year, price):
        self.model = model
        self.make = make
        self.year = year
        self.price = price
        Car.car_count += 1

    def get_car_info(self):
        return f"Model: {self.model}, Make: {self.make}, Year: {self.year}, Price: {self.price}"

    def calculate_depreciation(self):
        current_year = datetime.now().year 
        depreciation = self.price / (current_year - self.year)    #depreciation is the price divided by the number of years since the car was made
        return depreciation
    
    @staticmethod     #this method does not take any arguments
    def print_car_count():
        print (f"Total number of cars: {Car.car_count}")

    @classmethod      #this method takes the class as the first argument
    def compare_price(cls, car1, car2):
        if car1.price > car2.price:
            print(f"{car1.model} is more expensive than {car2.model}")
        elif car1.price < car2.price:
            print(f"{car1.model} is cheaper than {car2.model}")
        else:
            print(f"{car1.model} and {car2.model} have the same price")
        
car1 = Car("Model S", "Tesla", 2020, 80000)
car2 = Car("Model 3", "Tesla", 2021, 50000)

print(car1.get_car_info())
print(car2.get_car_info())

print(f"Car depraciation is: {car1.calculate_depreciation()}")
print(f"Car depraciation is: {car2.calculate_depreciation()}")

Car.print_car_count()

print (Car.compare_price(car1, car2))