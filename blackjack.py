import random, easygui
finish = False
def stand():
    stood = True
    diff_cards = False
    while diff_cards == False:
        pc_suit = random.choice(suits)
        pc_value = random.choice(values)
        pc_card = f"{pc_value}"+f"{pc_suit}"
        if pc_card == user_cards[0] or pc_card == user_cards[1] or pc_card == pc_cards[0]:
            diff_cards = False
        else:
            pc_cards.append(pc_card)
            diff_cards = True
        if pc_value == "Jack" or pc_value == "Queen" or pc_value == "King":
            pc_value_int2 = 10
        elif pc_value == "Ace":
            pc_value_int2 = 1
        else:
            pc_value_int2 = pc_value
        pc_value_int_total = pc_value_int1 + pc_value_int2
        easygui.msgbox(f"Pc cards = {pc_cards}")
        easygui.msgbox(f"Pc total = {pc_value_int_total}")
        
def hit():
    stood = False
    diff_cards = False
    while diff_cards == False:
        user_suit = random.choice(suits)
        user_value = random.choice(values)
        user_card = f"{user_value}"+f"{user_suit}"
        if user_card == user_cards[0] or user_card == user_cards[1] or user_card == pc_cards[0]:
            diff_cards = False
        else:
            user_cards.append(user_card)
            diff_cards = True

            #hit card conversion
            if user_value == "Jack" or user_value == "Queen" or user_value == "King":
                user_value_int3 = 10
            elif user_value == "Ace":
                user_value_int3 = 1
            else:
                user_value_int3 = user_value
            user_value_int_total = user_value_int1 + user_value_int2 + user_value_int3    
            easygui.msgbox(f"User cards = {user_cards}")
            easygui.msgbox(f"User total = {user_value_int_total}")
def bust_calc():
    if user_value_int_total > 21:
        bust = True
        print("busto")
        finish = True
pc_value_int_total = 0
suits = ["Hearts","Clubs","Spades","Diamonds"]
values = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
user_cards = []
pc_cards = []
bust = False

#1st user card
user_suit = random.choice(suits)
user_value = random.choice(values)
user_card = f"{user_value}"+f"{user_suit}"
user_cards.append(user_card)

#1st pc card
diff_cards = False
while diff_cards == False:
    pc_suit = random.choice(suits)
    pc_value = random.choice(values)
    if pc_value == user_cards[0]:
        pc_suit = random.choice(suits)
        pc_value = random.choice(values)
        diff_cards = False
    else:
        pc_cards.append(f"{pc_value}"+f"{pc_suit}")
        diff_cards = True
        break
easygui.msgbox(f"User = {user_cards}")
easygui.msgbox(f"Pc = {pc_cards}")


#first card conversion
if pc_value == "Jack" or pc_value == "Queen" or pc_value == "King":
    pc_value_int1 = 10
elif pc_value == "Ace":
    pc_value_int1 = 1
else:
    pc_value_int1 = pc_value

if user_value == "Jack" or user_value == "Queen" or user_value == "King":
    user_value_int1 = 10
elif user_value == "Ace":
    user_value_int1 = 1
else:
    user_value_int1 = user_value


#user card #2
diff_cards = False
while diff_cards == False:
    user_suit = random.choice(suits)
    user_value = random.choice(values)
    user_card = f"{user_value}"+f"{user_suit}"
    if user_card == user_cards[0] or user_card == pc_cards[0]:
        diff_cards = False   
    else:
        user_cards.append(user_card)
        diff_cards = True
        break
easygui.msgbox(f"user = {user_cards}")


#second card conversion
if user_value == "Jack" or user_value == "Queen" or user_value == "King":
    user_value_int2 = 10
elif user_value == "Ace":
    user_value_int2 = 1
else:
    user_value_int2 = user_value
user_value_int_total = user_value_int2 + user_value_int1
easygui.msgbox(f"User total = {user_value_int_total}")


#1st choice
choice = easygui.buttonbox("What do you want to do?", choices = ["Hit","Stand"])

if choice == "Hit":
    hit()
    #hit card conversion
    if user_value == "Jack" or user_value == "Queen" or user_value == "King":
        user_value_int3 = 10
    elif user_value == "Ace":
        user_value_int3 = 1
    else:
        user_value_int3 = user_value
    user_value_int_total = user_value_int1 + user_value_int2 + user_value_int3    
    easygui.msgbox(f"User cards = {user_cards}")
    easygui.msgbox(f"User total = {user_value_int_total}")

#Stand, reveal pc card
else:
    stand()
    finish = True

#check for bust
bust_calc()

if finish != True:
    #2nd choice
    msg = "What do you want to do?"
    choice = easygui.buttonbox(msg, choices = ["Hit","Stand"])
    if choice == "Hit":
        hit()
        #hit card conversion
        if user_value == "Jack" or user_value == "Queen" or user_value == "King":
            user_value_int4 = 10
        elif user_value == "Ace":
            user_value_int4 = 1
        else:
            user_value_int4 = user_value
        user_value_int_total = user_value_int1 + user_value_int2 + user_value_int3 + user_value_int4   
        easygui.msgbox(f"User cards = {user_cards}")
        easygui.msgbox(f"User total = {user_value_int_total}")
    else:
        stand()
        finish = True

    #check for bust
    bust_calc()

    #3rd choice
if finish != True:
    choice = easygui.buttonbox("What do you want to do?", choices = ["Hit","Stand"])
    if choice == "Hit":
        hit()
    #hit card conversion
        if user_value == "Jack" or user_value == "Queen" or user_value == "King":
            user_value_int5 = 10
        elif user_value == "Ace":
            user_value_int5 = 1
        else:
            user_value_int3 = user_value
        user_value_int_total = user_value_int1 + user_value_int2 + user_value_int3 + user_value_int4 + user_value_int5   
        easygui.msgbox(f"User cards = {user_cards}")
        easygui.msgbox(f"User total = {user_value_int_total}")
    else:
        stand()
        finish = True
    #check for bust
    bust_calc()
if bust == True:
    result = "You went over 21! You lose"
elif bust == False and finish == True:
    if pc_value_int_total > user_value_int_total and pc_value_int_total < 21:
        result = "You stood and pc has a higher number. You lose"
    elif pc_value_int_total < user_value_int_total and user_value_int_total < 21:
        result = "You win!"
easygui.msgbox(result)