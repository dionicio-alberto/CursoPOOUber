from account import Account
from uberX import UberX

if __name__ == "__main__":
    print("Hello word")
    
    uber1 = UberX("ABC123",Account("Emilio Escalante","ESXE981106"),"Toyota","Yaris")
    print(vars(uber1))
    print(vars(uber1.driver))
    