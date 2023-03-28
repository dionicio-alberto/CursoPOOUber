from car import Car
from account import Account

if __name__ == "__main__":
    print("Hello word")
    
    car = Car("XYZW789",Account("Beto Benitez","BEXB981106"))
    car.passenger = 5
    print(vars(car))
    print(vars(car.driver))
    