import easygui

name = easygui.enterbox("What is your name?")
easygui.msgbox(f"Hello, {name}")

age = easygui.integerbox("How old are you?")
easygui.msgbox(f"You are {age} years old")

school = easygui.buttonbox("Do you like school?", choices=["yes","no","yucky"])

if school == "yes":
    easygui.msgbox(f"You're a nerd {name}")
elif school == "no":
    easygui.msgbox("Sad little child")
else:
    easygui.msgbox("Daas fuego fam")
