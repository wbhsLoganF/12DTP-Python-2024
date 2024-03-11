import easygui
import random



def paper_scissors_rock():


    options = ["Rock", "Paper", "Scissors"]
    user_score = 0
    pc_score = 0
    result = "error"
    easygui.msgbox("Welcome to paper scissors rock!")

    while user_score < 5 and pc_score < 5:
        user = easygui.buttonbox("Choose wisely",choices = options)
        pc = random.choice(options)
        if user == "Rock" and pc == "Scissors" or user == "Paper" and pc == "Rock" or user == "Scissors" and pc == "Paper":
            result = "You win!"
            user_score += 1
        elif user == "Rock" and pc == "Paper" or user == "Paper" and pc == "Scissors" or user == "Scissors" and pc == "Rock":
            result = "You lose."
            pc_score += 1
        else:
            result = "A draw."

        easygui.msgbox(f"You picked {user} and I picked {pc}. {result}")
        easygui.msgbox(f"The score is {user_score} to you and {pc_score} to me")


#paper_scissors_rock()





def rock_paper_scissors_lizard_spock():


    options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    user_score = 0
    pc_score = 0
    result = "error"
    special = False
    easygui.msgbox("Welcome to rock paper scissors lizard spock!")

    while user_score < 5 and pc_score < 5:
        user = easygui.buttonbox("Choose wisely",choices = options)
        pc = random.choice(options)
        if user == "Rock" and pc == "Scissors" or user == "Paper" and pc == "Rock" or user == "Scissors" and pc == "Paper":
            result = "You win!"
            user_score += 1
        elif user == "Rock" and pc == "Paper" or user == "Paper" and pc == "Scissors" or user == "Scissors" and pc == "Rock":
            result = "You lose."
            pc_score += 1

        elif user == "Rock" and pc == "Lizard":
            result = "Your Rock crushed my Lizard. You win!"
            user_score += 1
            special = True
        elif user == "Rock" and pc == "Spock":
            result = "My Spock vapourised your Rock. You lose."
            pc_score += 1
            special = True
        elif user == "Paper" and pc == "Lizard":
            result = "My Lizard ate your Paper. You lose."
            pc_score += 1
            special = True
        elif user == "Paper" and pc == "Spock":
            result = "Your paper disproved my Spock. You Win!"
            user_score +=1
            special = True
        elif user == "Scissors" and pc == "Lizard":
            result = "Your Scissors decapitated my Lizard. You win!"
            user_score += 1
            special = True
        elif user == "Scissors" and pc == "Spock":
            result = "My Spock smashed your Scissors. You lose."
            pc_score += 1
            special = True
        elif user == "Lizard" and pc == "Rock":
            result = "My Rock crushed your Lizard. You lose."
            pc_score += 1
            special = True
        elif user == "Lizard" and pc == "Paper":
            result = "Your lizard ate my Paper. You win!"
            user_score +=1
            special = True
        elif user == "Lizard" and pc == "Scissors":
            result = "My scissors decapitated your Lizard. You lose."
            pc_score += 1
            special = True
        elif user == "Lizard" and pc == "Spock":
            result = "Your Lizard poisoned my Spock. You win!"
            user_score += 1
            special = True
        elif user == "Spock" and pc == "Paper":
            result = "My Paper disproved your Spock. You lose."
            pc_score +=1
            special = True
        elif user == "Spock" and pc == "Scissors":
            result = "Your Spock smashed my Scissors. You win!"
            user_score += 1
            special = True
        elif user == "Spock" and pc == "Rock":
            result = "Your Spock vapourised my Rock. You win!"
            user_score += 1
            special = True
        elif user == "Spock" and pc == "Lizard":
            result = "My Lizard poisoned your Spock. You lose."
            pc_score +=1
            special = True
        else:
            result = "A draw."
            special = False
        if special == True:
            easygui.msgbox(result)
            easygui.msgbox(f"The score is {user_score} to you and {pc_score} to me")
        else:
            easygui.msgbox(f"You picked {user} and I picked {pc}. {result}")
    if user_score == 5:
        easygui.msgbox("Winner!")
    else:
        easygui.msgbox("You lost this time")

rock_paper_scissors_lizard_spock()

