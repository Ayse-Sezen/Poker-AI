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




originalCardSet = [(1, H), (2, H), (3, H), (4, H), (5, H), (6, H), (7, H), (8, H), (9, H), (10, H), (J, H), (Q, H), (K, H),
                   (1, D), (2, D), (3, D), (4, D), (5, D), (6, D), (7, D), (8, D), (9, D), (10, D), (J, D), (Q, D), (K, D),
                   (1, C), (2, C), (3, C), (4, C), (5, C), (6, C), (7, C), (8, C), (9, C), (10, C), (J, C), (Q, C), (K, C),
                   (1, S), (2, S), (3, S), (4, S), (5, S), (6, S), (7, S), (8, S), (9, S), (10, S), (J, S), (Q, S), (K, S)]

deck = [(1, H), (2, H), (3, H), (4, H), (5, H), (6, H), (7, H), (8, H), (9, H), (10, H), (J, H), (Q, H), (K, H),
        (1, D), (2, D), (3, D), (4, D), (5, D), (6, D), (7, D), (8, D), (9, D), (10, D), (J, D), (Q, D), (K, D),
        (1, C), (2, C), (3, C), (4, C), (5, C), (6, C), (7, C), (8, C), (9, C), (10, C), (J, C), (Q, C), (K, C),
        (1, S), (2, S), (3, S), (4, S), (5, S), (6, S), (7, S), (8, S), (9, S), (10, S), (J, S), (Q, S), (K, S)]

holeCardsList = []
communityCardsList = []

# // Player is 0, AI is 1
dealerButton = 1

user = User()
ai = Ai()

pot = 0

userBet = 0
aiBet = 0

userHand = []
aiHand = []

for i in range(7):
    # Hand out hole cards
    # Make a random number generator between 0 and len(deck) four times, 2 for player and 2 for AI
    # Check to make sure you're not getting the card multiple times (pop picked cards from deck)

    for i in range(2):
        deckLength = len(deck)
        card = deck.pop(random.randrange(deckLength))
        ai.holeCards.append(card)

    for i in range(2):
        deckLength = len(deck)
        card = deck.pop(random.randrange(deckLength))
        user.holeCards.append(card)
        # Randomly choose a number between 0 and len(deck)
        # Pop card from deck and push into holeCardsList
        #loop back up and get next card
 


    # Hand out dealer button
    # Alternate the button between two players, always starting with the user getting the dealer button first, then if the user got it on previous round
    #the AI gets it on the next round
        
    # if player had button on last round, give button to AI
    if dealerButton == 0:
        dealerButton = 1
    elif dealerButton == 1:
        dealerButton = 0


    # Betting Round 1

    # Dealer makes mandatory bet (small blind) or exits game
    # AI will handle betting on it's own
    # Give user prompts for betting

    # if dealer is the user, prompt user to make choices, get user input for a choice, and then take action based off of that (if else statements)
    if dealerButton == 0:
        pass

    # if dealer is the ai, run ai's code to place a bet
    elif dealerButton == 1: 
        pass


    #Non dealer makes mandatory bet (big blind) or exits game
    # if dealer is the user, make the AI do the big blind bet
    if dealerButton == 0:
        # make AI do big blind bet (just doubling the bet of the user, unless ai doesn't have enough money to do so, in which it's game over(?)
        pass

    # if dealer is the AI, make user do big blind bet
    elif dealerButton == 1:
        # make user do big blind bet
        pass


    # Deal out three com cards
    # Again, randomly generate numbers, index into the deck, pop cards out of deck and into comCards
    for i in range(3):
        # Randomly choose a number between 0 and len(deck)
        # Pop card from deck and push into communityCardsList
        communityCardsList.append(deck.pop(random.randrange(len(deck))))
        # loop back up and get next card




    # Betting Round 2

    # Dealer's choices: Fold, Call, Raise, exit game
    # if Dealer is AI:
        # AI will do this based off of what? Figure out how the AI will evaluate the community cards and pick a choice.
    # elif Dealer is User:
        # User makes their own choice, prompt user for choice and take in input and process it
    # if the choice is to fold, then give other (non-dealer) player all the money and then continue back up to the loop (aka short circuit this and go loop back up)

    # Non Dealer's choices: Fold, Call, Raise, exit game
    # same as above, do the ssame stuff for AI and for player here



    # Deal out 2 com cards
    # Rand num generator
    for i in range(2):
    # Randomly choose a number between 0 and len(deck)
    # Pop card from deck and push into communityCardsList
        communityCardsList.append(deck.pop(random.randrange(len(deck))))
    # loop back up and get next card


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

    # Compare Hands
    # Just compare card combo numbers returned back with hands from newSort, player with the highest hand wins
    if userHand[1] > aiHand[1]:
        # user wins pot, add pot to user's money
        user.winnings += pot
    elif aiHand[1] > userHand[1]:
        # ai wins the pot, add pot to ai's money
        ai.winnings += pot
    else:
        # draw, no one wins
        pass

    # Reset card deck, put all cards back in the deck
    deck = originalCardSet

    ai.clearHand()
    user.clearHand()

    userBet = 0
    aiBet = 0
    pot = 0 

    userHand.clear()
    aiHand.clear()



