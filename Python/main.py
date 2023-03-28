from car import Car


if __name__ == "__main__":
    print("Hello word")
    
    car = Car()
    car.license = "XYZW789"
    car.driver = "Beto Benitez"
    car.id = 11244
    car.passenger = 5
    print(vars(car))
    
    car2 = Car()
    car2.license = "GGH542"
    car2.driver = "Camilia Cardenas"
    car2.id = 11241
    car2.passenger = 3
    print(vars(car2))
    