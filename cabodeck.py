from carddeck import CardDeck
from card import Card

class CABODeck(CardDeck):

    def __init__(self):

        # this dict connects card values with [numOfCardsInDeck, associatedAction]
        caboDict = {
            0: [2, 'none'],
            1: [4, 'none'],
            2: [4, 'none'],
            3: [4, 'none'],
            4: [4, 'none'],
            5: [4, 'none'],
            6: [4, 'none'],
            7: [4, 'peek'],
            8: [4, 'peek'],
            9: [4, 'spy'],
            10: [4, 'spy'],
            11: [4, 'swap'],
            12: [4, 'swap'],
            13: [2, 'none']
        }

        # this will temporarily hold all of the cards and is then passed to constructor
        # of superclass
        cards = []
        for value in caboDict:
            numOfCardsInDeck, associatedAction = caboDict[value]

            for i in range(numOfCardsInDeck):
                currentCard = Card(value=value, action=associatedAction)
                cards.append(currentCard)

        super().__init__(cards=cards)