class Card:

    def __init__(self, value=0, action='none'):
        self.value = value
        self.action = action

        # check if card is set up correctly
        self.performCheck()


    # checks data types of action and value
    # error is printed if something went wrong
    def performCheck(self):
        validValues = [num for num in range(0, 14)]
        validActions = ['swap', 'peek', 'spy', 'none']

        if self.value not in validValues:
            raise ValueError('Card value is not valid!')
        if self.action not in validActions:
            raise ValueError('Card action is not valid!')


    # get and set methods
    def getCardValue(self):
        return self.value


    def setCardValue(self, value=0):
        self.value = value
        self.performCheck()


    def getCardAction(self):
        return self.action


    def setCardAction(self, action='none'):
        self.action = action
        self.performCheck()


    def __str__(self):
        valueText = 'Value: ' + str(self.value)
        actionText = 'Action: ' + self.action
        return valueText + ', ' + actionText

