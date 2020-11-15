from random import shuffle

class CardDeck:

    def __init__(self, cards=[]):
        self.cards = cards


    # shuffles the deck
    def shuffleCards(self):
        shuffle(self.cards)


    # dremoves and returns card at a given position
    def drawCard(self, position=0):
        card = self.cards.pop(position)
        return card


    # does the same as drawCard, but card is not removed from deck
    def lookAtFirstCard(self):
        card = self.cards[0]
        return card


    # returns number of cards left in deck
    def getCount(self):
        return len(self.cards)


    # this function inserts a card at given position
    def addCard(self, card, position:int):
        self.cards.insert(card, position)
        
        
    # replaces a card at a given position
    def replaceCard(self, newCard, position:int):
        self.cards[position] = newCard
        