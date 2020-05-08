from newSort import rateHand
import random


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


class Agent:
    
    def __init__(self):
        self.holeCardsList = []
        self.foldFlag = 0
        #self.winnings = 10000 # I changed this from 0 to 10k so that agents have money to play with
        #self.handScore = 0

    def getHoleCards(self):
        return self.holeCardsList

    def getHandScore(self, holeCardsList, communityCardsList):
        if self.foldFlag:
            return 0
        bestHand = rateHand(communityCardsList, holeCardsList)
        self.hand = bestHand[0]
        self.handScore = bestHand[1]
        return self.handScore

    def clearHand(self):
        self.holeCardsList = []
        self.handScore = 3
        self.foldFlag = 0



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
        # print("Please press b to place an initial bet")
        print("testing AI places an initial bet")
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
        # print("Please press b to bet, c to check, or f to fold")
        print("the test ai will press b to bet, c to check, or f to fold")
        print("The pot is {0} and it must bet {1}".format(state[2], state[1]))
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
        # print("")
        # print("Your bankroll is {}".format(self.winnings))
        # print("You must bet at least {}".format(under))
        # print("")
        # print("How much would you like to bet? Press q to cancel bet")        
        print("Test AI bankroll is {}".format(self.winnings))
        print("Test AI must bet at least {}".format(under))
        print("")
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
                print("the test ai is betting {}".format(self.bet))
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

        hscore = 0
        self.bet = self.placeBets(state, 1, hscore)
        self.winnings -= self.bet

        print("Ai placed an initial bet of {}".format(self.bet))
        print("")

        return self.bet

        # make sure you record this initial bet somewhere because user class will need to know what it is


    def move(self, state, userBet, bigBlindFlag, holeCardsList, communityCardsList):
        if bigBlindFlag:
            # ai has to at least match double of user's bet
            doubleBet = userBet * 2
            doubleBet = max(state[1], doubleBet)
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
            return random.randrange(200, 500)
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
                

class ImprovedAi(Agent):
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

        hscore = 0
        if self.holeCardsList[0][0] == self.holeCardsList[1][0]:
            hscore += 4
        if self.holeCardsList[0][1] == self.holeCardsList[1][1]:
            hscore += 2
        hscore += ((self.holeCardsList[0][0] + self.holeCardsList[1][0])//4)
        self.bet = self.placeBets(state, 1, hscore)
        self.winnings -= self.bet

        print("Ai placed an initial bet of {}".format(self.bet))
        print("")

        return self.bet

        # make sure you record this initial bet somewhere because user class will need to know what it is

    def move(self, state, userBet, bigBlindFlag, holeCardsList, communityCardsList):
        if bigBlindFlag:
            # ai has to at least match double of user's bet
            doubleBet = state[1] * 2
            if doubleBet > self.winnings:  # if double of player's bet is greater than the initial amount the ai has to play with
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
            self.handScore = self.calculateBestHand(
                holeCardsList, communityCardsList)
            self.bet = self.placeBets(state, 0, self.handScore)

        print("Ai is placing a bet of {}".format(self.bet))
        print("")
        return self.bet

    def calculateBestHand(self, holeCardsList, communityCardsList):
        hand = []
        handScore = 0
        if len(communityCardsList) == 5:
            hand, handScore == rateHand(holeCardsList, communityCardsList)
        else:
            testDeck = deck
            for i in range(2):
                if holeCardsList[i] in testDeck:
                    testDeck.remove(holeCardsList[i])
            
            for i in range(len(communityCardsList)):
                if communityCardsList[i] in testDeck:
                    testDeck.remove(communityCardsList[i])
            
            sumScore = 0
            counter = 1
            for _ in range(5-len(communityCardsList)):
                for i in range(len(testDeck)):
                    tempCCList = communityCardsList + [testDeck[i]]
                    counter+=1
                    hand, tempscore = rateHand(holeCardsList, tempCCList)
                    sumScore += tempscore
            handScore = sumScore//counter

        return handScore

    def placeBets(self, state, smallBlindFlag, handScore):
        # if ai is placing bets for a small blind, make bet within a certain range
        userWinnings = state[0]
        userBet = state[1]
        pot = state[2]
        if smallBlindFlag:
            sbBet = self.winnings//200
            self.bet = max(random.randrange(200, 500), sbBet*(20, 50))
            print("AI is betting {}".format(self.bet))
            return self.bet
        else:
            if ((self.handScore < 2) and (pot > self.winnings//2)):
                self.foldFlag = 1
                print("AI folded")
                return 0
                # fold
            if self.handScore <= 4:  # if hand is in lower 5 hand ranks
                # Call
                self.bet = userBet
                self.winnings -= self.bet
                print("AI is betting {}".format(self.bet))
                return self.bet
            elif self.handScore > 4 and self.handScore <= 6:
                # Raise
                self.bet = random.randint(userBet+pot//6, userBet+200+pot//6)
                self.winnings -= self.bet
                print("AI is betting {}".format(self.bet))
                return self.bet
            elif self.handScore > 6:
                self.bet = random.randint(
                    userBet+pot//3+userWinnings//10, userBet+pot//2+userWinnings//10)
                self.winnings -= self.bet
                print("AI is betting {}".format(self.bet))
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
    # us.showBoard(ccl, pot, ai)
    state = [pot, under, ccl]
    newPot = us.move(state)
    print("result = ", newPot)


if __name__ == "__main__":
    testUser(10, 4)

