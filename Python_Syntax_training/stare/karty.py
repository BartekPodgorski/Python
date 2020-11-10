import random

cardList = ["9","9","9","9","10","10","10","10",
            "Jack","Jack","Jack","Jack",
            "Queen","Queen","Queen","Queen",
            "King","King","King","King",
            "Ace", "Ace", "Ace", "Ace",
            "Joker","Joker"]
print(cardList)
random.shuffle(cardList)
player1 = "player1"
player2 = "player2"
hand_one = []
hand_two = []

def give_cards(deck,amount,player):
    pojemnik = []
    i = 0
    if (player == player1):
        pojemnik = hand_one
    elif(player == player2):
        pojemnik = hand_two
    else:
        print("error")
    while i < amount:        
        x = 0
        x = deck.pop()
        pojemnik.append(x)
        i += 1
    
    
give_cards(cardList,5,player1)
give_cards(cardList,5,player2)
