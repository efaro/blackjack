import random

def createDeck():
    suits = ["hearts", "diamonds", "clubs", "spades"]
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
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
    return value, numAces
def main():
    deck = createDeck()
    playerHand = [deck.pop(), deck.pop()]
    dealerHand = [deck.pop(), deck.pop()]
    cashBalance = 1000                                      # maybe implement some sort of input in the form of a deposit

    while cashBalance > 0:
        currBet = int(input("Place your bets please: "))    # bets placed
        #playerCards = 
        print(f"Balance: ${cashBalance - currBet}")         # print new balance after bet is placed
        #dealerCards = dealerHand[1]["rank"] + dealerHand[1]["suit"][0]
        print(f"Dealer shows:  {dealerHand[1]}")            # show the second card dealt to the dealer
        print(f"You show: {playerHand}")                    # show both of the players cards
        
        playerVal, _ = calculateHand(playerHand)            # calculate the value of the players hand
        dealerVal, _ = calculateHand(dealerHand)            # calculate the value of the dealers hand

        if playerVal == 21:                                 # checking for blackjack from player
            print("Blackjack!")
            cashBalance += 1.5 * currBet
            break

        # check right away if dealer has blackjack, ask for insurance if the up-card is an ace

        if dealerVal == 21 and dealerHand[1]['rank'] != 'ace':              # check if dealer has 21 and their up-card is not an ace
            print(f"Dealer: {dealerHand}")
            print("Dealer has blackjack.")                                  # end the round
            cashBalance -= currBet                                          # current bet subtracted from balance
            break
        if dealerHand[1]['rank'] == 'ace':                                  # if the dealer's up-card is an ace ask for insurance
            insurance = input("Would you like insurance? (Y/N): ")
            if insurance.lower() == 'y':                                    # if accepted, deduct half of the current bet
                insuranceBet = currBet/2
                cashBalance -= insuranceBet                                 # insurance bet subtracted
                print(f"Balance: ${cashBalance}")
            if dealerVal == 21:
                print(f"Dealer: {dealerHand}")
                print("Dealer has blackjack.")
                if insurance.lower() == 'n':
                    cashBalance -= currBet                            # calculation only carried out when decision is made
                    cashBalance += 2 * insuranceBet
                break
            else:
                print("Nobody home!")
        
        # while playerVal < 22:
        #     action = input("Do you want to hit")
        #     if playerVal == 21:
        #         break

main()


