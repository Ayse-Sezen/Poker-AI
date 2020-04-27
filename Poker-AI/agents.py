from newSort import rateHand

class Agent:
    
    def __init__(self):
        self.holeCards = []
        self.winnings = 10000 # I changed this from 0 to 10k so that agents have money to play with
        self.handScore = 0

    def getHoleCards(self):
        return self.holeCards

    def getHandScore(self, communityCardsList):
        bestHand = rateHand(communityCardsList, self.holeCards)
        self.handScore = bestHand[1]
        return self.handScore

    def clearHand(self):
        self.holeCards = []
        self.handScore = 0



class User(Agent):
    bet = 0
    hand = ()

    def __init__(self):
        super().__init__()

    def smallBlind(self, state):
        print("Please press b to place an initial bet")
        choice = input()

        if choice == 'b':
            return self.placeBet(state)
        else:
            print("Please picka valid option")
            self.move(state)
    
    # state = [pot, amount needed to bet, comCardList]
    # return value is the amount added to the pot that the opponent needs to match
    def move(self, state): 
        print("Please press b to bet, c to check, or f to fold")
        print("The pot is {0} and you must bet {1}".format(state[0], state[1]))
        choice = input()
        if choice == 'b':
            return self.placeBet(state)
        elif choice == 'c':
            if state[1] > 0:
                print("You cannot check while the other player has more money in the pot")
                self.move(state)
            return 0
        elif choice == 'f':
            return "fold"
        else:
            print("Please pick a valid option")
            self.move(state)

    def placeBet(self, state):
        under = state[1]
        print("Your bankroll is {}".format(self.winnings))
        print("You must bet at least {}".format(under))
        print("How much would you like to bet? Press q to cancel bet")
        betStr = input()
        if betStr == 'q':
            self.move(state)
        else:
            bet = int(betStr)
            if bet < under:
                self.placeBet(state)
            elif bet > self.winnings:
                print("You do not have that much money")
                self.placeBet(state)
            else: # screw try catch for bad inputs 
                self.winnings -= bet
                return bet - under




class Ai(Agent):
    bet = 0
    hand = ()

    def __init__(self):
        super().__init__()

    def smallBlind(self, state):
        print("Ai is placing small blind...")

        bet = placeBets(state, 1)
        winnings -= bet # **************** Do you reference this as winnings or as agent.winnings?

        print("Ai placed an initial bet of {}".format(bet))

        return bet

        # make sure you record this initial bet somewhere because user class will need to know what it is


    def move(self, state, bigBlindFlag, holeCardsList, communityCardsList):
        if bigBlindFlag:
            # ai has to at least match double of user's bet
            doubleBet = state[0] * 2

            if doubleBet > initialAmt:
                # forfeit game or pass on this round?
            else:
                print("Ai is placing big blind...")
                bet = doubleBet
                winnings -= bet
        else:
            # place bets according to rank of card hand for this round
            # lower hand ranking = lower bet
            print("Ai is placing bets...")
            handScore = getHandScore(holeCardsList, communityCardsList)
            bet = placeBets(state, 0, handScore)

            
        print("Ai is placing a bet of {}".format(bet))
        return bet
                    


    def placeBets(self, state, smallBlindFlag, handScore):
        # if ai is placing bets for a small blind, make bet within a certain range
        if smallBlindFlag:
            return randint(200, 500)
        else:
             if handScore <= 5: # if hand is in lower 5 hand ranks
                # Call
                 bet = state[0]
                 winnings -= bet
                 return bet
            elif handScore > 5 and handScore <= 10:
                # Raise
                bet = randint(state[0], initialAmt)
                winnings -= bet
                return bet
                


# Global getHandScore function
def getHandScore(holeCardsList, communityCardsList):
    hand = rateHand(communityCardsList, holeCardsList)
    return hand[1]






    

# user class test
def testUser(pot, under):
    us = User()
    us.winnings = 22
    ai = Ai()
    ai.winnings = 13
    ccl = ["ccard1", "ccard2", "ccard3"]
    us.holeCards = ["hcard1", "hcard2"]
    us.showBoard(ccl, pot, ai)
    state = [pot, under, ccl]
    newPot = us.move(state)
    print("result = ", newPot)


if __name__ == "__main__":
    testUser(10, 4)

