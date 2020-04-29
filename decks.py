from BlackJackGame import cards
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(cards.Card(suit,rank))

    def __str__(self):
        printer = ''
        for d in self.deck:
            printer += '\n'+d.__str__()
        return 'The Deck has following cards'+printer

    def deal(self):
        temp = self.deck.pop()
        return temp

    def shuffle(self):
        random.shuffle(self.deck)
