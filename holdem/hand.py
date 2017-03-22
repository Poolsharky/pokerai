
################################################################################
class hand():
    def __init__(self, playerParent):
        self.playerParent = playerParent

        #self.fullHand = None

        self.bestHand = None

        self.hand_rank = -1
        self.highCard = -1


        # 9 Royal flush
        # 8 Straight flush
        # 7 Four of a Kind
        # 6 Full house
        # 5 Flush
        # 4 Straight
        # 3 Three of a kind
        # 2 Two pair
        # 1 Pair
        # 0 Nothing

    ##################################################
    def updateHand(self, totalHand):
        royalFlush = self.checkRoyalFlush(totalHand)
        straightFlush = self.checkStraightFlush(totalHand)
        fourOfKind = self.checkFourOfKind(totalHand)
        fullHouse = self.checkFullHouse(totalHand)
        flush = self.checkFlush(totalHand)
        straight = self.checkStraight(totalHand)
        threeOfKind = self.checkThreeOfKind(totalHand)
        twoPair = self.checkTwoPair(totalHand)
        pair = self.checkPair(totalHand)

        #TODO ace can be high or low for streights

        if(royalFlush != False):
            self.hand_rank = 9
            self.highCard = self.findHighCard(royalFlush)
        elif(straightFlush != False):
            self.hand_rank = 8
            self.highCard = self.findHighCard(straightFlush)
        elif(fourOfKind != False):
            self.hand_rank = 7
            self.highCard = self.findHighCard(fourOfKind)
        elif(fullHouse != False):
            self.hand_rank = 6
            self.highCard = self.findHighCard(fullHouse)
        elif(flush != False):
            self.hand_rank = 5
            self.highCard = self.findHighCard(flush)
        elif(straight != False):
            self.hand_rank = 4
            self.highCard = self.findHighCard(straight)
        elif(threeOfKind != False):
            self.hand_rank = 3
            self.highCard = self.findHighCard(threeOfKind)
        elif(twoPair != False):
            self.hand_rank = 2
            self.highCard = self.findHighCard(twoPair)
        elif(pair != False):
            self.hand_rank = 1
            self.highCard = self.findHighCard(pair)
        else:
            self.hand_rank = 0
            self.highCard = self.findHighCard(totalHand)

    ##################################################
    def checkRoyalFlush(self, totalHand):
        return False

        #This one is easy there are only 4 combintation that match.
        #check for those combinations.


    ##################################################
    def checkStraightFlush(self, totalHand):
        return False
    #check streight, put the streight in to a separate array
    # then check that array for a flush.

    ##################################################
    def checkFourOfKind(self, totalHand):
        return False
        totalHand.sort(key = lambda card: card.ind_val)

        trips_found = 0
        for i in range(0, len(totalHand) - 3):
            if(totalHand[i].ind_val == totalHand[i + 1].ind_val
               and totalHand[i].ind_val == totalHand[i + 2].ind_val
                and totalHand[i].ind_val == totalHand[i + 3].ind_val):
                return True

        return False

    ##################################################
    def checkFullHouse(self, totalHand):
        return False
        totalHand.sort(key = lambda card: card.ind_val, reverse=True)
        for card in totalHand:
            print(card.ind_val)
        print("moo...")


        #TODO:
        #what if its a situation where we have 3 of a kind and 3 of kind together.
        #not sure if that needs to be handled. might not make a difference

        #2,2,3,3,3 vs 2,2,4,4,4,
        #2,2,3,3,3 vs 2,2,2,4,4,



        three_of_a_kind_found = False
        #first find three of a kind and remove from deck.
        for i in range(0, len(totalHand) - 2):
            #print(totalHand[i].ind_val)
            if(totalHand[i].ind_val == totalHand[i + 1].ind_val and totalHand[i].ind_val == totalHand[i + 2].ind_val):
                three_of_a_kind_found =  True

                print(totalHand[i].ind_val,",",totalHand[i + 1].ind_val,",",totalHand[i + 2].ind_val)

                totalHand.pop(i)
                totalHand.pop(i)
                totalHand.pop(i)

                break


        print("moo2...")
        for card in totalHand:
            print(card.ind_val)

        #then try to find a pair and remove from hand
        if(three_of_a_kind_found):
            for i in range(0, len(totalHand) - 1):
                if(totalHand[i].ind_val == totalHand[i + 1].ind_val):
                    return True

        return False

    #fisr check for a pair and remove it from array put it in a diferent array
    #then find a 3 of a kind and remove that.


    ##################################################
    def checkFlush(self, totalHand):
        return False
        totalHand.sort(key = lambda card: card.suit)
        for i in range(0, len(totalHand) - 4):
            if(totalHand[i].suit == totalHand[i + 1].suit and totalHand[i].suit == totalHand[i + 2].suit
                and totalHand[i].suit == totalHand[i + 3].suit and totalHand[i].suit == totalHand[i + 4].suit):
                return True

        return False

    ##################################################
    def checkStraight(self, totalHand):
        return False
        totalHand = list(totalHand)
        indexesToPop = []

        for i in range(0, len(totalHand)):
            for j in range(i+1, len(totalHand)):
                if(totalHand[i].ind_val == totalHand[j].ind_val):
                    indexesToPop.append(j)

        for ind in indexesToPop:
            totalHand.pop(ind)

        totalHand.sort(key = lambda card: card.ind_val)

        if(len(totalHand) < 5):
            return False
        elif(len(totalHand) == 5):
            for i in range(0, len(totalHand) - 5):
                if(totalHand[i].ind_val == (totalHand[i + 1].ind_val - 1)
                    and totalHand[i].ind_val == (totalHand[i + 2].ind_val - 2)
                    and totalHand[i].ind_val == (totalHand[i + 3].ind_val - 3)
                    and totalHand[i].ind_val == (totalHand[i + 4].ind_val - 4)):
                    return [totalHand[i], totalHand[i + 1], totalHand[i + 2], totalHand[i + 3], totalHand[i + 4]]
        elif(len(totalHand) == 6):
            for i in range(0, len(totalHand) - 4):
                if(totalHand[i].ind_val == (totalHand[i + 1].ind_val - 1)
                    and totalHand[i].ind_val == (totalHand[i + 2].ind_val - 2)
                    and totalHand[i].ind_val == (totalHand[i + 3].ind_val - 3)
                    and totalHand[i].ind_val == (totalHand[i + 4].ind_val - 4)):
                    return [totalHand[i], totalHand[i + 1], totalHand[i + 2], totalHand[i + 3], totalHand[i + 4]]
        elif(len(totalHand) == 7):
            for i in range(0, len(totalHand) - 3):
                if(totalHand[i].ind_val == (totalHand[i + 1].ind_val - 1)
                    and totalHand[i].ind_val == (totalHand[i + 2].ind_val - 2)
                    and totalHand[i].ind_val == (totalHand[i + 3].ind_val - 3)
                    and totalHand[i].ind_val == (totalHand[i + 4].ind_val - 4)):
                    return [totalHand[i], totalHand[i + 1], totalHand[i + 2], totalHand[i + 3], totalHand[i + 4]]

        return False

    ##################################################
    def checkThreeOfKind(self, totalHand):
        totalHand = list(totalHand)
        totalHand.sort(key = lambda card: card.ind_val, reverse=True)

        for i in range(0, len(totalHand) - 2):
            if(totalHand[i].ind_val == totalHand[i + 1].ind_val and totalHand[i].ind_val == totalHand[i + 2].ind_val):
                return [totalHand[i], totalHand[i + 1], totalHand[i + 2]]

        return False

    ##################################################
    def checkTwoPair(self, totalHand):
        totalHand = list(totalHand)
        totalHand.sort(key = lambda card: card.ind_val, reverse=True)
        newHand = []
        pairs_found = 0
        for i in range(0, len(totalHand) - 1):
            if(totalHand[i].ind_val == totalHand[i + 1].ind_val):
                pairs_found += 1
                newHand.append(totalHand[i])
                newHand.append(totalHand[i + 1])
                i+=1

        if(pairs_found == 2):
            return newHand
        else:
            return False

    ##################################################
    def checkPair(self, totalHand):
        totalHand = list(totalHand)
        totalHand.sort(key = lambda card: card.ind_val, reverse=True)

        for i in range(0, len(totalHand) - 1):
            if(totalHand[i].ind_val == totalHand[i + 1].ind_val):
                return [totalHand[i], totalHand[i + 1]]

        return False

    ##################################################
    def findHighCard(self, totalHand):
        #print(totalHand[0].ind_val)
        totalHand.sort(key = lambda card: card.ind_val, reverse=True)
        return totalHand[0].ind_val