from newSort import rateHand

class Agent:
    
    def __init__(self):
        self.holeCards = []
        self.winnings = 0
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

    def __init__(self):
        super().__init__()

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

    def __init__(self):
        super().__init__()


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
