from carddeck import CardDeck
from card import Card
from cabodeck import CABOdeck



class Player:

	def __init__(initialCards:CardDeck):
		
		# Intially, the player receives a card deck containing 4 random cards from the deck
		self.cards = intialCards

		# The first two cards are known to him!
		self.knowledge = [
			self.cards[0],
			self.cards[1],
			None,
			None
		]


	def playRound(visibleCard):
		a = 10


	def endGame():
		a = 10 
