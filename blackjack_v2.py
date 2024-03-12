import random, easygui

"""CONSTANTS"""
suits = ["Hearts","Clubs","Spades","Diamonds"]
values = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]


"""EMPTY CONTAINERS"""
user_cards = []
pc_cards = []
user_values = []
pc_values = []

"""FIRST 2 CARDS FOR USER"""
for i in range (0,2):
    user_suit = random.choice(suits)
    user_value = random.choice(values)
    user_values.append(user_value)
    user_card = f"{user_value}"+f" of {user_suit}"
    if user_card in user_cards:
        print("e")
    else:
        user_cards.append(user_card)
print(user_cards)


"""FIRST 2 CARDS FOR PC"""
for i in range (0,2):
    pc_suit = random.choice(suits)
    pc_value = random.choice(values)
    pc_values.append(pc_value)
    pc_card = f"{pc_value}"+f" of {pc_suit}"
    if pc_card in pc_cards:
        print("e")
    else:
        pc_cards.append(pc_card)
print(pc_cards)


"""USER CONVERSION"""
for i in user_values:
    if i == "Jack" or i == "Queen" or i == "King":
        print("e")