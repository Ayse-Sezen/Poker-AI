class Agent:
    
    def __init__(self):
        self.holeCards = []
        self.winnings = 0

    def getHand(self):
        return self.holeCards

    def clearHand(self):
        self.holeCards = []



class User(Agent):

    def __init__(self):
        super().__init__()


class Ai(Agent):

    def __init__(self):
        super().__init__()
