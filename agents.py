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



class User(Agent):

    def __init__(self):
        super().__init__()


class Ai(Agent):

    def __init__(self):
        super().__init__()
