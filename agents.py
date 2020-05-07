from newSort import rateHand
import random


class Agent:
    
    def __init__(self):
        self.holeCardsList = []
        #self.winnings = 10000 # I changed this from 0 to 10k so that agents have money to play with
        #self.handScore = 0

    def getHoleCards(self):
        return self.holeCardsList

    def getHandScore(self, holeCardsList, communityCardsList):
        bestHand = rateHand(communityCardsList, holeCardsList)
        self.hand = bestHand[0]
        self.handScore = bestHand[1]
        return self.handScore

    def clearHand(self):
        self.holeCardsList = []
        self.handScore = 0



class User(Agent):
    bet = 0
    hand = []
    handScore = 0
    winnings = 20000
    holeCardsList = []

    def __init__(self):
        super().__init__()

    def smallBlind(self, state):
        print("")
        print("Please press b to place an initial bet")
        #choice = input()
        choice = 'b'

        if choice == 'b':
            return self.placeBet(state)
        else:
            print("Please pick a valid option")
            return self.move(state)
    
    # state = [pot, amount needed to bet, comCardList]
    # return value is the amount added to the pot that the opponent needs to match
    def move(self, state):
        x = 0
        print("")
        print("Please press b to bet, c to check, or f to fold")
        print("The pot is {0} and you must bet {1}".format(state[0], state[1]))
        #choice = input()
        choice = 'b'
        if choice == 'b':
            return self.placeBet(state)
        elif choice == 'c':
            if state[1] > 0:
                print("")
                print("You cannot check while the other player has more money in the pot")
                print("")
                return self.move(state)
            return x
        elif choice == 'f':
            #return "fold"
            return x
        else:
            print("Please pick a valid option")
            return self.move(state)
        return x

    def placeBet(self, state):
        #under = state[1]
        under = 200
        print("")
        print("Your bankroll is {}".format(self.winnings))
        print("You must bet at least {}".format(under))
        print("")
        print("How much would you like to bet? Press q to cancel bet")
        #betStr = input()
        bet = random.randint(under, 2000)
        betStr = str(bet)
        if betStr == 'q':
            self.move(state)
        else:
            self.bet = int(betStr)
            if self.bet < under:
                self.placeBet(state)
            elif self.bet > self.winnings:
                print("You do not have that much money")
                return self.placeBet(state)
            else: # screw try catch for bad inputs 
                self.winnings -= self.bet
                return self.bet
                #return self.bet - under




class Ai(Agent):
    bet = 0
    hand = []
    handScore = 0
    winnings = 20000
    holeCardsList = []
    amtWon = 0
    amtLost = 0

    def __init__(self):
        super().__init__()
        

    def smallBlind(self, state):
        print("")
        print("Ai is placing small blind...")

        self.bet = placeBets(state, 1)
        self.winnings -= self.bet # **************** Do you reference this as winnings or as agent.winnings?

        print("Ai placed an initial bet of {}".format(self.bet))
        print("")

        return self.bet

        # make sure you record this initial bet somewhere because user class will need to know what it is


    def move(self, state, userBet, bigBlindFlag, holeCardsList, communityCardsList):
        if bigBlindFlag:
            # ai has to at least match double of user's bet
            doubleBet = userBet * 2
            if doubleBet > self.winnings: # if double of player's bet is greater than the initial amount the ai has to play with
                # forfeit game or pass on this round?
                pass
            else:
                print("")
                print("Ai is placing big blind...")
                self.bet = doubleBet
                self.winnings -= self.bet
        else:
            # place bets according to rank of card hand for this round
            # lower hand ranking = lower bet
            print("")
            print("Ai is placing bets...")
            self.handScore = self.getHandScore(holeCardsList, communityCardsList)
            self.bet = self.placeBets(userBet, 0, self.handScore)

            
        print("Ai is placing a bet of {}".format(self.bet))
        print("")
        return self.bet
                    


    def placeBets(self, userBet, smallBlindFlag, handScore):
        # if ai is placing bets for a small blind, make bet within a certain range
        if smallBlindFlag:
            return randint(200, 500)
        else:
             if self.handScore <= 5: # if hand is in lower 5 hand ranks
                # Call
                 self.bet = userBet
                 self.winnings -= self.bet
                 return self.bet
             elif self.handScore > 5 and self.handScore <= 7:
                # Raise
                self.bet = random.randint(userBet, userBet+200)
                self.winnings -= self.bet
                return self.bet
             elif self.handScore > 7:
                 self.bet = random.randint(userBet+200, userBet+600)
                 self.winnings -= self.bet
                 return self.bet
                


# Global getHandScore function
#def getHandScore(self, holeCardsList, communityCardsList):
 #   self.hand = rateHand(communityCardsList, holeCardsList)
  #  return self.hand[1]






    

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

