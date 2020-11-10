import random
#Deck 
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

#Flag to continue play
play_longer = True

#Creating all cards
class Card:

	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
	    return self.rank + ' of ' + self.suit
#Creating deck, shuffle function and deal which give one card
class Deck:

	def __init__(self):
		self.deck = [] #Blank list for deck
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		single_card = self.deck.pop()
		return single_card

#Creating the hand of player
class Hand:

	def __init__(self):
		self.cards = [] #Blank list for cards from hand
		self.value = 0 #Value of all cards
		self.aces = 0 #Flag on Ace

	def add_card(self,card):
		self.cards.append(card)
		self.value += values[card.rank]
		if card.rank == 'Ace':
			self.aces = 1

	#If we find an Ace in hand and our value of hand is higher than 21 we reduce value of Ace from 11 to 1
	def choice_ace(self):
		while self.value > 21 and self.aces:
			self.value -= 10
			self.aces -= 1

#Class which is responsible for bets
class Money:

	def __init__(self):
		self.total = 100 # default value of money
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet

#Functions

#Function responsible for value of bets
#If it is not integer you have to try again
def take_bet(player_money):
	while True:
		try:
			player_money.bet = int(input("How many money do you want to bet? "))
		except ValueError:
			print("It have to be integer amount")
		else:
			if player_money.bet >  player_money.total:
				print(f"Sorry you don't have enough money. Your total money is {player_money.total}")
			else:
				break

#Function responsible for take extra cards
def hit(deck,player):
	player.add_card(deck.deal())
	player.choice_ace()

#Function responsible for player decision about take card (hit is upper) or stay
def hit_or_stay():
	global play_longer
	while True:
		x = input("If you want to hit click 'h', if you want to stay click 's': ")
		if x == 'h':
			hit(deck,player)
			#Statement for next try
			if player.value > 21:
				break
			else:
				first_show(player,blackleg)
				print("Do you want to try again?")
				continue
		elif x == 's':
			print("Player stands. Dealer is playing.")
			play_longer = False #stop play change flag
			break
		else:
			print("Sorry, try again")
			continue
		

#In BlackJack in first show blackleg(dealer) don't show you one card
def first_show(player,blackleg):
	print("\nYour cards are:", *player.cards , sep ="\n")
	print("\nBlackleg card:", blackleg.cards[0], sep ="\n")

#Final show all cards and value of hands
def show_all(player,blackleg):
	print("\nPlayer cards are:", *player.cards , sep ="\n")
	print("Player values are", player.value, "\n")
	print("\nBlackleg cards are:", *blackleg.cards , sep ="\n")
	print("Blackleg values are", blackleg.value, "\n")

#Function of scenarios
def player_lose(player, blackleg, money):
	print("Player lose!")
	money.lose_bet()

def blackleg_win(player, blackleg, money):
	print("Blackleg win!")
	money.lose_bet()

def blackleg_lose(player, blackleg, money):
	print("Blackleg lose!")
	money.win_bet()

def player_win(player, blackleg, money):
	print("Player win!")
	money.win_bet()

def push(player,blackleg):
	 print("Blackleg and Player tie! It's a push.")

#MAIN LOOP
while True:

	#Create the deck
	deck = Deck()
	#Shuffle the deck
	deck.shuffle()
	#Create a player and add two cards
	player = Hand()
	player.add_card(deck.deal())
	player.add_card(deck.deal())
	#Create a blackleg and add two cards
	blackleg = Hand()
	blackleg.add_card(deck.deal())
	blackleg.add_card(deck.deal())
	#Initialization of player money
	player_money = Money()
	#Make the value of bet
	take_bet(player_money)
	#Information about money
	print(f"Welcome in Bart BlackJack.\nYou have {player_money.total}$")
	#First show of cards
	first_show(player,blackleg)
	#Loop with decision of player
	while play_longer:

		hit_or_stay()
		#Check on players value , if it is hidher than 21 player lose
		if player.value > 21:

			show_all(player,blackleg)
			player_lose(player,blackleg,player_money)
			break

		else:
			#If blackleg has samller value than 16 he hit.
			while blackleg.value <= 17:
				hit(deck,blackleg)

			show_all(player,blackleg)

			if blackleg.value > 21:
				blackleg_lose(player, blackleg, player_money)

			elif blackleg.value > player.value:
				blackleg_win(player, blackleg, player_money)

			elif blackleg.value < player.value:
				player_win(player,blackleg,player_money)

			else:
				push(player,blackleg)

	print("\nPlayers winnings stand at: ", player_money.total)

	new_game = input("If you want to play new game click 'y', if not click 'n': ")
	if new_game == 'y':
		play_longer = True
		continue
	elif new_game == 'n':
		print("Thank you for playing!")
		break
	else:
		print("Invalid key")
		break