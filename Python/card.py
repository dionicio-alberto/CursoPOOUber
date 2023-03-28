from payment import Payment

class Card(Payment):
    number      = int
    cvv         = int
    date        = int
    
    def __init__(self, id, number, cvv, date):
        super().__init__(id)
        self.cvv    = cvv
        self.number = number
        self.date   = date