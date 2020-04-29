from BlackJackGame import decks
from BlackJackGame import hands
from BlackJackGame import chips

playing = True


def take_bet(player_chips):
    while True:
        try:
            player_chips.bet = int(input('How many chips would you like to bet?'))
        except:
            print('Sorry, a bet must be an integer!')
        else:
            if player_chips.bet > player_chips.total:
                print("Sorry, your bet can't exceed", player_chips.total)
            else:
                break


def show_some(player_hand, dealer_hand):
    print("\nDealer's Hand :")
    print('<card hidden>')
    print(dealer_hand.cards_owned[1])
    print("\n Player's Hand ",*player_hand.cards_owned,sep='\n')


def show_all(player_hand, dealer_hand):
    print("\nDealer's Hand :", *dealer_hand.cards_owned, sep='\n')
    print("Dealer's Value   ", dealer_hand.total)
    print("\n Player's Hand ", *player_hand.cards_owned, sep='\n')
    print("Player's Value   ", player_hand.total)


def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.ace_check()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

        if x[0].lower() == 'h':
            hit(deck, hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break


def player_busts(player_chips):
    print("Player busts!")
    player_chips.lose()


def player_wins(player_chips):
    print("Player wins!")
    player_chips.win()


def dealer_busts(player_chips):
    print("Dealer busts!")
    player_chips.win()


def dealer_wins(player_chips):
    print("Dealer wins!")
    player_chips.lose()


def push():
    print("Dealer and Player tie! It's a push.")


player_chips = chips.Chips()

while True:

    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
       Dealer hits until she reaches 17. Aces count as 1 or 11.')

    deck = decks.Deck()
    deck.shuffle()

    player_hand = hands.Hand()
    dealer_hand = hands.Hand()

    # Giving 2 cards to player
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    # Giving 2 cards to dealer

    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Enter your bet
    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while playing:
        hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.total > 21:
            player_busts(player_chips)
            break

    if player_hand.total <= 21:
        while dealer_hand.total < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.total > 21:
            dealer_busts(player_chips)
        elif dealer_hand.total > player_hand.total:
            dealer_wins(player_chips)
        elif dealer_hand.total < player_hand.total:
            player_wins(player_chips)
        else:
            push()

    print("\nPlayer's winnings stand at", player_chips.total)

    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break
