def createDeck():
    suits = ["hearts", "diamonds", "clubs", "spades"]
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
    deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def calculateHand(hand):
    value = 0
    numAces = 0
    for card in hand:
        rank = card['rank']
        if rank in ['jack', 'queen', 'king']:
            value += 10
        elif rank == 'ace':
            value += 11
            numAces = 1
        else:
            value += int(rank)
    
    while value > 21 and numAces > 0:
        value -= 10
        numAces -= 1
    return value

def main():
    deck = createDeck()
    playerHand = [deck.pop(), deck.pop()]
    dealerHand = [deck.pop(), deck.pop()]
    cashBalance = 1000                      # maybe implement some sort of input in the form of a deposit

    while cashBalance > 0:
        currBet = input("Place your bets please: ")
        print("Dealer shows: ", dealerHand[1])
        print("You show", playerHand)

        # Cases

        # Hit

        # Double

        #
        


