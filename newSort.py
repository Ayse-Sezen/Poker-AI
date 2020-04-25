A = 14
K = 13
Q = 12
J = 11

H = 'Hearts'
D = 'Diamonds'
C = 'Clubs'
S = 'Spades'



# Each function will return a tuple (hand, card combo number):
#      - The hand will be a list of the cards that make up that card combo or an empty tuple if that card combo was not found
#      - The card combo number will just be a number indicating what card combo we found; this will be useful for the AI/Player using this program


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

def sort(communityCardsList, holeCardsList):
    # we leave the hole cards list alone since it's only two cards
    cardDict = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], J:[], Q:[], K:[], A:[]}

    for card in communityCardsList:
        for entry in cardDict:
            if entry == card[0]:
                cardDict[entry].append((card[1], "Community"))
                break

    for card in holeCardsList:
        for entry in cardDict:
            if entry == card[0]:
                cardDict[entry].append((card[1], "Hole"))
    # Royal Flush Test
    #cardList = royalFlush(cardDict, holeCardsList)
    #print(cardList)

     # Two Pair Test
    cardList = twoPair(cardDict, holeCardsList)
    print(cardList)




    

"""
    # Royal Flush Test
    cardList = royalFlush(cardDict, holeCardsList)
    print(cardList)

# Straight Flush Test
cardList = straightFlush(cardDict, holeCardsList)
print(cardList)


    # Four of a Kind Test
    cardList = fourOfAKind(cardDict, holeCardsList)
    print(cardList)

    # Full House Test
    cardList = fullHouse(cardDict, holeCardsList)
    print(cardList)

    # Flush Test
    cardList = flush(cardDict, holeCardsList)
    print(cardList)

    # Straight Test
    cardList = straight(cardDict, holeCardsList)
    print(cardList)

    # Three of a Kind Test
    cardList = threeOfAKind(cardDict, holeCardsList)
    print(cardList)

    # Two Pair Test
    cardList = twoPair(cardDict, holeCardsList)
    print(cardList)

    # One Pair Test
    cardList = onePair(cardDict, holeCardsList)
    print(cardList)

    # High Card Test
    cardList = highCard(cardDict, holeCardsList)
    print(cardList)
"""

def royalFlush(cardDict, holeCardsList):
    flag = False
    hand = [] # an empty list to build the hand we're going to return (if we find it)
    holeCtr = 0 # counter for how many hole cards we've seen while searching for royal flush pattern
    communityCtr = 0 # same as above but for community cards
    x = 10 # to use later when we loop through dictionary, we start at entries for card value 10 while looking for 10, J, Q, K A sequence
    
    # Check if our two hole cards have the same suit (because if not, then we exit)
    if holeCardsList[0][1] == holeCardsList[1][1]:
        # if they do have the same suit, see if they match any of the 10, J, K, Q, A cards in a Royal Flush
        if holeCardsList[0][0] == 10 or J or Q or K or A:
            if holeCardsList[1][0] == 10 or J or Q or K or A:
                flag = True
            else:
                #return []
                return "Error: Your second hole card did not match the 10, J, Q, K, A values"
        else:
            #return []
            return "Error: Your first hole card did not match the 10, J, Q, K, A values"


    if flag:
        for x in range(10, A+1):
            # check to see if cards exist in the dictionary for the card value x
            if x in cardDict:
                # search through entries to look for cards that have the same suit as our hole cards
                for card in cardDict[x]:
                    # if a card of the same suit as our hole card exists in the dict
                    if card[0] == holeCardsList[0][1]:
                        # add it to the hand in the form of a tuple (x = card value, cardDict[x][y][0] = suit)
                        hand.append((x, card[0]))
                        
                        # check if it was a hole or community card
                        if card[1] == "Hole":
                            holeCtr+=1
                        else:
                            communityCtr+=1
            else:
                # if entries don't exist for that card value in the dict, then our 10, J, K, Q, A pattern was broken
                #return []
                return "Error: Entries don't exists for that card value in the dict"


        # if, after the for loop, we have the proper cards, return the hand
        if len(hand) == 5:
            if holeCtr == 2 and communityCtr == 3:
                return (hand, 10)
            else:
                #return []
                return "Error: Did not have two hole and three community cards"
        else: # if for whatever reason the hand does not have a length of 5 (which is should, otherwise it's an error)
            print("Royal Flush Error: Hand did not have a length of 5")
            print(len(hand))
            return ()



def straightFlush(cardDict, holeCardsList):
    hand = []
    holeCtr = 0
    comCtr = 0
    ctr = 0
    holeCard = 0
    comCard = 0

    for x in cardDict:
        if cardDict[x]:
            for card in cardDict[x]:
                if card[0] == holeCardsList[0][1]:
                    if card[1] == "Hole":
                        if not holeCard:
                            holeCard = (x, card[0])
                            holeCtr += 1
                            break
                    else:
                        if not comCard:
                            comCard = (x, card[0])
                            comCtr += 1
            if holeCard:
                hand.append(holeCard)
            else:
                hand.append(comCard)

            # reset these for the next iteration of outer for loop
            holeCard = 0
            comCard = 0

            ctr += 1
            if ctr == 5:
                if holeCtr == 2 and comCtr == 3:
                    return (hand, 9)
                else:
                    hand.pop(0)
        else:
            if hand:
                hand.clear()
                ctr = 0
                holeCtr = 0
                comCtr = 0
    return ()



    
def fourOfAKind(cardDict, holeCardsList):
    hand = []
    holeCtr = 0
    holeCardTuple = 0
    comCardTuple = 0

    for x in cardDict:
        if len(cardDict[x]) == 4:
            for card in cardDict[x]:
                if card[1] == "Hole":
                    holeCtr += 1
                    holeCardTuple = (x, card[0])
                hand.append((x, card[0]))
        else:
            if not comCardTuple:
                if cardDict[x]:
                    for card in cardDict[x]:
                        if card[1] == "Community":
                            comCardTuple = (x, card[0])
                            break

        if holeCtr == 2:
            hand.append(comCardTuple)
            return (hand, 8)
        elif holeCtr == 1:
            if holeCardTuple != holeCardsList[0]:
                hand.append(holeCardsList[0])
                return (hand, 8)
            else:
                hand.append(holeCardsList[1])
                return (hand, 8)
    return ()


def fullHouse(cardDict, holeCardsList):
    hand = []
    foundPair = False
    foundThreeOfAKind = False
    
    # if our hole cards make up a pair
    if holeCardsList[0][0] == holeCardsList[1][0]:
        for card in cardDict[holeCardsList[0][0]]:
            hand.append((holeCardsList[0][0], card[0]))
        # check if part of a three of a kind
        if len(cardDict[holeCardsList[0][0]]) == 3:
            foundThreeOfAKind = True
        else:
            foundPair = True

        if foundThreeOfAKind:
            # we need to find a pair
            for x in cardDict:
                if len(cardDict[x]) == 2:
                    for card in cardDict[x]:
                        hand.append((x, card[0]))
                    return (hand, 7)

        elif foundPair:
            # we need to find a three of a kind
            for x in cardDict:
                if len(cardDict[x]) == 3:
                    for card in cardDict[x]:
                        hand.append((x, card[0]))
                    return (hand, 7)
    else: # two hole cards are not part of a pair
        # one of them will be aprt of a pair and the other will be part of a three of a kind
        for card in cardDict[holeCardsList[0][0]]:
            hand.append((holeCardsList[0][0], card[0]))
        if len(hand) == 2:
            foundPair = True
        elif len(hand) == 3:
            foundThreeOfAKind = True

        if foundPair: # next hole card should be part of a three of a kind, so check for that
            if len(cardDict[holeCardsList[1][0]]) == 3:
                for card in cardDict[holeCardsList[1][0]]:
                    hand.append((holeCardsList[1][0], card[0]))
                return (hand, 7)
            else:
                return ()

        elif foundThreeOfAKind: # next hole card should be part of a pair, so check for that
            if len(cardDict[holeCardsList[1][0]]) == 2:
                for card in cardDict[holeCardsList[1][0]]:
                    hand.append((holeCardsList[1][0], card[0]))
                return (hand, 7)
            else:
                return ()
        else:
            return ()
    return ()  

                

def flush(cardDict, holeCardsList):
    hand = []
    ctr = 0
    
    if holeCardsList[0][1] == holeCardsList[1][1]: # if they are the same suit
        hand.append(holeCardsList[0])
        hand.append(holeCardsList[1])

        # search dictionary for 3 community cards of same suit
        for x in cardDict:
            if cardDict[x]: # if cards exist in the dictionary for card value x
                for card in cardDict[x]:
                    # if the card has the same suit as our hole cards
                    if card[0] == holeCardsList[0][1]:
                        # and the card is a community card
                        if card[1] == "Community":
                            # then add it to the hand
                            hand.append((x, card[0]))
                            ctr += 1

                            # if we've counted and added 3 community cards to our hand then we're done
                            if ctr == 3:
                                return (hand, 6)
    return ()


def straight(cardDict, holeCardsList):
    hand = []
    holeCtr = 0
    comCtr = 0
    ctr = 0
    holeCard = 0
    comCard = 0

    for x in cardDict:
        if cardDict[x]:
            for card in cardDict[x]:
                if card[1] == "Hole":
                    if not holeCard:
                        holeCard = (x, card[0])
                        holeCtr += 1
                        break
                else:
                    if not comCard:
                        comCard = (x, card[0])
                        comCtr += 1
            if holeCard:
                hand.append(holeCard)
            else:
                hand.append(comCard)

            # reset these for the next iteration of outer for loop
            holeCard = 0
            comCard = 0

            ctr += 1
            if ctr == 5:
                if holeCtr == 2 and comCtr == 3:
                    return (hand, 5)
                else:
                    hand.pop(0)
        else:
            if hand:
                hand.clear()
                ctr = 0
                holeCtr = 0
                comCtr = 0
    return ()


    
def threeOfAKind(cardDict, holeCardsList):
    hand = []
    holeCtr = 0
    holeCard = 0
    comCard1 = 0
    comCard2 = 0

    # find three cards of the same value
    # tally up how many hole cards there are in those three
    # find cards to make up for the rest

    for x in cardDict:
        if len(cardDict[x]) == 3:
            for card in cardDict[x]:
                hand.append((x, card[0]))
                if card[1] == "Hole":
                    holeCtr += 1
                    if not holeCard:
                        holeCard = (x, card[0])
        else:
            if cardDict[x]:
                for card in cardDict[x]:
                    if card[1] == "Community":
                        if not comCard1:
                            comCard1 = (x, card[1])
                        elif not comCard2:
                            comCard2 = (x, card[1])
    if len(hand) == 3:
        if holeCtr == 2: # we need to add two com cards to the hand
            hand.append(comCard1)
            hand.append(comCard2)
            return (hand, 4)
        elif holeCtr == 1: # we need to add a hole card + a com card
            hand.append(comCard1)
            for card in holeCardsList:
                if card != holeCard:
                    hand.append(card)
                    return (hand, 4)
        elif holeCtr == 0: # we need to add both hole cards to hand
            hand.append(holeCardsList[0])
            hand.append(holeCardsList[1])
            return (hand, 4)

    return ()
                    


def twoPair(cardDict, holeCardsList):
    extraComCard = 0
    comCardPair = []
    hand = []

    # first we find a pair made up of community cards and we find an extra community card
    for x in cardDict:
        if len(cardDict[x]) >= 2:
            for card in cardDict[x]:
                if card[1] == "Community":
                    # if we don't have a com card pair yet, we build one
                    if len(comCardPair) <= 2:
                        comCardPair.append((x, card[0]))
                    else:
                        # if we've already found our community card pair, then find one more extra community card and save that off
                        if not extraComCard:
                            extraComCard = (x, card[0])
                # if we've found what we need then break out of inner for loop
                if len(comCardPair) == 2 and extraComCard:
                    break
                else:
                    # we have to clear out the comCardPair because we need to have
                    # our pair be from the same value, and on the next iteration of the 'for card in cardDict[x]' loop we'll be on a
                    # different card value, so we're just erasing it to start over
                    comCardPair.clear()
        else: # if cardDict[x] did not have a length of 2
            # but entries still exist for card value x in the dictionary
            # and we still don't have our extra com card
            # then find an extra com card and save that off (trust me, we'll need this later, there's a method to my madness here)
            if cardDict[x] and not extraComCard:
                for card in cardDict[x]:
                    if card[1] == "Community":
                        extraComCard = (x, card[0])
                        break
        # if we've found what we needed then break out of outer for loop
        if len(comCardPair) == 2 and extraComCard:
            break

    # next we check to see if our hole cards make up a pair themselves or not

    # if they do...
    if holeCardsList[0][0] == holeCardsList[1][0]:
        # then we can just stick the community card pair and the extra community card we found earlier into the hand along
        # with the hole cards and return that
        hand.append(holeCardsList[0])
        hand.append(holeCardsList[1])
        hand.append(comCardPair[0])
        hand.append(comCardPair[1])
        hand.append(extraComCard)
        print("Returning from holeCards being a pair")
        return (hand, 3)

    # however, if they don't make up a pair...
    else:
        if len(comCardPair) == 2: # if we found the community card pair, then we know that one of our hole cards should be pair of a hole/com pair
            hand.append(comCardPair[0])
            hand.append(comCardPair[1])

            # find which hole card is part of a hole/com pair and then append it to the hand
            if len(cardDict[holeCardsList[0][0]]) >= 2: # if first hole card was part of a pair
                hand.append(holeCardsList[0]) # append the hole card
                for card in cardDict[holeCardsList[0][0]]: # find the other card in it's pair
                    if card[1] == "Community": # and it's a community card
                        hand.append((holeCardsList[0][0], card[0])) # append it into hand
                        hand.append(holeCardsList[1]) # put other hole card into the hand
                        break
            # if it wasn't the first hole card, then it should be the second
            elif len(cardDict[holeCardsList[1][0]]) >= 2:
                hand.append(holeCardsList[1])
                for card in cardDict[holeCardsList[1][0]]:
                    if card[1] == "Community":
                        hand.append((holeCardsList[1][0], card[0]))
                        hand.append(holeCardsList[0])
                        break
                    

            # check to see if the hand is full, and if so then return
            if len(hand) == 5:
                print("Returning from one com card pair and one hole/com pair")
                return (hand, 3)
            else:
                return () # means we didn't find a hole/com pair

            
        else: # if we didn't find a community card pair then both of our hole cards are part of a hole/com pair
            # get hole/com pair from first hole card
            if len(cardDict[holeCardsList[0][0]]) >= 2: # if first hole card was part of a pair
                hand.append(holeCardsList[0]) # append the hole card
                for card in cardDict[holeCardsList[0][0]]: # find the other card in it's pair
                    if card[1] == "Community": # and it's a community card
                        hand.append((holeCardsList[0][0], card[0])) # append it into hand
                        break # get out of loop
            # get hole/com pair from second hole card
            if len(cardDict[holeCardsList[1][0]]) >= 2:
                hand.append(holeCardsList[1])
                for card in cardDict[holeCardsList[1][0]]:
                    if card[1] == "Community":
                        hand.append((holeCardsList[1][0], card[0]))
                        break

            # hand should now have h, c, h, c cards
            # add one more community card
            hand.append(extraComCard)

            # make sure length of hand is 5 because if not then we didn't find both hole/com pairs
            if len(hand) == 5:
                print("Returning from two hole/com pairs")
                return (hand, 3)
            else:
                return ()
    return ()

                        




        






    
def onePair(cardDict, holeCardsList):
    hand = []
    ctr =  0
    foundPair = False

    # two hole cards are the pair
    if holeCardsList[0][0] == holeCardsList[1][0]:
        hand.append(holeCardsList[0])
        hand.append(holeCardsList[1])

        for x in cardDict:
            if cardDict[x]:
                for card in cardDict[x]:
                    if card[1] == "Community":
                        hand.append((x, card[0]))
                        ctr += 1

                        if ctr == 3:
                            return (hand, 2)
    # one of the hole cards must be part of the pair
    else:
        if len(cardDict[holeCardsList[0][0]]) >= 2:
            hand.append(holeCardsList[0])
            for card in cardDict[holeCardsList[0][0]]:
                if card[1] == "Community":
                    hand.append((holeCardsList[0][0], card[0]))
                    hand.append(holeCardsList[1])
                    foundPair = True
                    break
                
                
        elif len(cardDict[holeCardsList[1][0]]) >= 2:
            hand.append(holeCardsList[1])
            for card in cardDict[holeCardsList[1][0]]:
                if card[1] == "Community":
                    hand.append((holeCardsList[1][0], card[0]))
                    hand.append(holeCardsList[0])
                    foundPair = True
                    break

        ctr = 0
        
        for x in cardDict:
            if cardDict[x]:
                if x != holeCardsList[0][0] and x != holeCardsList[1][0]:
                    # if we found a pair already then we only need two com cards
                    for card in cardDict[x]:
                        if foundPair:
                            if card[1] == "Community":
                                hand.append((x, card[0]))

                                ctr += 1
                                if ctr == 2:
                                    return (hand, 2)
                        else: # if we did not find a pair
                            # then we find a pair of com cards and an extra com card and add in the hole cards
                            # code to find a pair of com cards
                            if len(cardDict[x]) >= 2:
                                if card[1] == "Community":
                                    hand.append((x, card[0]))
                                    ctr += 1

                                    if ctr == 2:
                                        break
                            else: # code to find an extra com card
                                if card[1] == "Community":
                                    hand.append((x, card[0]))
                                    ctr += 1

                                    if ctr == 3: # then we've appended our com pair and our extra com card, so add hole cards and return
                                        hand.append(holeCardsList[0])
                                        hand.append(holeCardsList[1])
                                        return (hand, 2)
    return ()
                            


def highCard(cardDict, holeCardsList):
    x = 14
    ctr = 0
    hand = []
    holeCardIsHighCard = False

    hand.append(holeCardsList[0])
    hand.append(holeCardsList[1])
    
    while x >= 0:
        if cardDict[x]: # if an entry exists for that value of x
            # check if there's a hole card as an entry for card value x
            if holeCardsList[0][0] == x or holeCardsList[1][0] == x:
                # if so then we need to search the rest of the dictionary for three more
                # community cards to add to the hand
                holeCardIsHighCard = True
                break
            else:
                hand.append((x, cardDict[x][0][0]))
                break
        else:
            x -= 1

    x -= 1

    
    while x >= 0:
        if cardDict[x]:
            for card in cardDict[x]:
                if card[1] == "Community":
                    hand.append((x, card[0]))
                    ctr += 1

                    if holeCardIsHighCard:
                        if ctr == 3:
                            return (hand, 1)
                    else:
                        if ctr == 2:
                            return (hand, 1)
        x-=1

    return ()

    



# Test runs
# Two pair
cardList = [(6, D), (Q, H), (K, S), (9, C)] # you need to make sure the same card from the same suit isn't entered twice
holeCardsList = [(6, H), (K, C)]
sort(cardList, holeCardsList)



"""
# Royal Flush
cardList = [(A, H), (Q, H), (K, H), (Q, D)] # you need to make sure the same card from the same suit isn't entered twice
holeCardsList = [(10, H), (J, H)]
sort(cardList, holeCardsList)

# Straight Flush
cardList = [(3, H), (5, H), (6, H), (8, D)] # you need to make sure the same card from the same suit isn't entered twice
holeCardsList = [(4, H), (7, H)]
sort(cardList, holeCardsList)



# 4 of a Kind
cardList = [(9, D), (9, C), (9, S), (Q, D)] # you need to make sure the same card from the same suit isn't entered twice
holeCardsList = [(9, H), (J, H)]
sort(cardList, holeCardsList)


# Full House
cardList = [(Q, C), (4, H), (4, D), (1, D)] # you need to make sure the same card from the same suit isn't entered twice
holeCardsList = [(Q, H), (Q, S)]
sort(cardList, holeCardsList)


# Flush
cardList = [(2, S), (Q, S), (9, S), (Q, D)] # you need to make sure the same card from the same suit isn't entered twice
holeCardsList = [(K, S), (8, S)]
sort(cardList, holeCardsList)


# Straight
cardList = [(6, C), (9, H), (8, S), (Q, D)] # you need to make sure the same card from the same suit isn't entered twice
holeCardsList = [(7, D), (5, H)]
sort(cardList, holeCardsList)


# Three of a Kind
cardList = [(10, D), (10, C), (6, D), (Q, D)] # you need to make sure the same card from the same suit isn't entered twice
holeCardsList = [(10, H), (J, S)]
sort(cardList, holeCardsList)


# Two Pair
cardList = [(8, H), (K, D), (8, S), (3, D)] # you need to make sure the same card from the same suit isn't entered twice
holeCardsList = [(K, H), (J, H)]
sort(cardList, holeCardsList)



# One Pair
cardList = [(6, D), (Q, H), (J, S), (9, C)] # you need to make sure the same card from the same suit isn't entered twice
holeCardsList = [(6, H), (K, C)]
sort(cardList, holeCardsList)



# High Card
cardList = [(A, H), (7, C), (5, S), (Q, D)] # you need to make sure the same card from the same suit isn't entered twice
holeCardsList = [(2, D), (3, H)]
sort(cardList, holeCardsList)
"""
