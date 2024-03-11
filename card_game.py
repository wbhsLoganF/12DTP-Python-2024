import random, easygui

suits = ["Hearts","Clubs","Spades","Diamonds"]
values = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]

diff_cards = False


while diff_cards == False:
    user_suit = random.choice(suits)
    user_value = random.choice(values)
    pc_suit = random.choice(suits)
    pc_value = random.choice(values)
    if user_value == pc_value and user_suit == pc_suit:
        diff_cards = False
    else:
        diff_cards = True


if pc_value == "Jack":
    pc_value_int = 11
elif pc_value == "Queen":
    pc_value_int = 12
elif pc_value == "King":
    pc_value_int = 13
elif pc_value == "Ace":
    pc_value_int = 14
else:
    pc_value_int = pc_value

if user_value == "Jack":
    user_value_int = 11
elif user_value == "Queen":
    user_value_int = 12
elif user_value == "King":
    user_value_int = 13
elif user_value == "Ace":
    user_value_int = 14
else:
    user_value_int = user_value



    if user_value_int > pc_value_int:
        result = "You win!"
    elif user_value_int < pc_value_int:
        result = "You lose"
    else:
        result = "A draw"




easygui.msgbox(f"I have the {pc_value} of {pc_suit}")
easygui.msgbox(f"You have the {user_value} of {user_suit}")
easygui.msgbox(result)
    
    
        

    
