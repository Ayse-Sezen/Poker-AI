import random
from agents import User, Ai

A = 14
K = 13
Q = 12
J = 11

H = 'Hearts'
D = 'Diamonds'
C = 'Clubs'
S = 'Spades'

deck = [(1, H), (2, H), (3, H), (4, H), (5, H), (6, H), (7, H), (8, H), (9, H), (10, H), (J, H), (Q, H), (K, H),
        (1, D), (2, D), (3, D), (4, D), (5, D), (6, D), (7, D), (8, D), (9, D), (10, D), (J, D), (Q, D), (K, D),
        (1, C), (2, C), (3, C), (4, C), (5, C), (6, C), (7, C), (8, C), (9, C), (10, C), (J, C), (Q, C), (K, C),
        (1, S), (2, S), (3, S), (4, S), (5, S), (6, S), (7, S), (8, S), (9, S), (10, S), (J, S), (Q, S), (K, S)]



# ******* Codes for each possible card combo *******
# 1 = High Card
# 2 = One Pair
# 3 = Two Pair
# 4 = Three of a Kind
# 5 = Straight
# 6 = Flush
# 7 = Full House
# 8 = Four of a Kind
# 9 = Straight Flush
# 10 = Royal Flush

def run(user, ai, deck):
    dealerButton = 1

    communityCardsList = []
    # Hand out hole cards
    # Make a random number generator between 0 and len(deck) four times, 2 for player and 2 for AI
    # Check to make sure you're not getting the card multiple times (pop picked cards from deck)

    for i in range(4):
        deckLength = len(deck)
        card = deck.pop(random.randrange(deckLength))
        if i < 2:
            ai.holeCards.append(card)
        else:
            user.holeCards.append(card)
 

    # Hand out dealer button
    # if player had button on last round, give button to AI
    if dealerButton == 0:
        dealerButton = 1
    elif dealerButton == 1:
        dealerButton = 0

    pot = 0

    # Betting Round 1

    # Dealer makes mandatory bet (small blind) or exits game

    # if dealer is the user, prompt user to make choices, get user input for a choice, and then take action based off of that (if else statements)
    if dealerButton == 0:
        user.smallBlind(state)
        #pass

    # if dealer is the ai, run ai's code to place a bet
    elif dealerButton == 1:
        ai.smallBlind(state)
        #pass


    # Non Dealer Makes Big Blind
    if dealerButton == 0:
        # make AI do big blind bet
        ai.move(state, 1, [], [])
        #pass
    elif dealerButton == 1:
        # make user do big blind bet
        user.move(state)
        #pass


    # Deal out three com cards
    for i in range(3):
        communityCardsList.append(deck.pop(random.randrange(len(deck))))




    # Betting Round 2

    # Dealer's choices: Fold, Call, Raise, exit game
    # if Dealer is AI:
        # AI will do this based off of what? Figure out how the AI will evaluate the community cards and pick a choice.
    # elif Dealer is User:
        # User makes their own choice, prompt user for choice and take in input and process it
    # if the choice is to fold, then give other (non-dealer) player all the money and then continue back up to the loop (aka short circuit this and go loop back up)

    # Dealer's choice
    if dealerButton == 0: # user
        user.move(state)
    elif dealerButton == 1: # ai
        ai.move(state, 0, holeCardsList, communityCardsList)

    # Non Dealer's choice
    if dealerButton == 0: # if user is dealer
        # ai makes next move
        ai.move(state, 0, holeCardsList, communityCardsList)

    elif dealerButton == 1: # if ai is dealer
        # user makes next move
        user.move(state)


    # Deal out 2 com cards
    # Rand num generator
    for i in range(2):
        communityCardsList.append(deck.pop(random.randrange(len(deck))))


    # Final Step: Generate hands and compare to see who won the pot
    # Dealer: Pick best hand
    # If Dealer is AI:
        # run community and hole cards through new sort
        # ai.getHand(communityCardsList)
    # If Dealer is User:
        # prompt user to pick 3 community cards, then run only those com cards and the user's hole cards through newSort
        # in order to identify what type of hand the user chose

    # Non Dealer: Picks best hand
        # same as above for AI and User hand building

    userScore = user.getHandScore(holeCardsList, communityCardsList)
    aiScore = ai.getHandScore(holeCardsList, communityCardsList)
    # Compare Hands
    # Just compare card combo numbers returned back with hands from newSort, player with the highest hand wins
    if userScore > aiScore:
        # user wins pot, add pot to user's money
        user.winnings += pot
    elif aiScore > userScore:
        # ai wins the pot, add pot to ai's money
        ai.winnings += pot
    else:
        # draw, no one wins
        user.winnings += pot//2
        user.winnings += pot//2
        # this rounds off uneven pots if that was possible

    ai.clearHand()
    user.clearHand()



def showBoard(communityCardsList, pot, user, ai):
    print("Your hand is: {}".format(user.holeCards))
    print("The board is: {}".format(communityCardsList))
    print("The pot is {}".format(pot))
    print("Your bankroll is {0} and the opponent's is {1}".format(user.winnings, ai.winnings))


if __name__ == "__main__":
    user = User()
    ai = Ai()

    # // Player is 0, AI is 1
    dealerButton = 1

    for i in range(7):
        run(user, ai, deck[:])

