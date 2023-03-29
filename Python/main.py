from account import Account
from uberX import UberX
from card import Card
from user import User

if __name__ == "__main__":
    print("Hello word")
    
    uber1 = UberX("ABC123",User("Emilio Escalante","ESXE981106"),"Toyota","Yaris")
    print(vars(uber1))
    print(vars(uber1.driver))
    
    pago1 = Card("DHE0001", 12345, 905, 1122)
    print(vars(pago1))
    
    uber1.driver.email="gatitoquelegustaelmambo_@gmail.com"
    print(vars(uber1.driver))
