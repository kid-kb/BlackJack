class Chips:
    def __init__(self,total=100):
        self.total=total
        self.bet=0

    def win(self):
        self.total+=2*self.bet

    def lose(self):
        self.total -= 2 * self.bet