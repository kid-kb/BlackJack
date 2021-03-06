from BlackJackGame import cards

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


class Hand:
    def __init__(self):
        self.cards_owned = []
        self.total = 0
        self.aces = 0

    def add_card(self, card):
        self.cards_owned.append(card)
        self.total += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def ace_check(self):
        if self.total > 21 and self.aces:
            self.total -= 10
            self.aces -= 1
