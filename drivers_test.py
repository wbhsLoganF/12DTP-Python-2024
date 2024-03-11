import easygui
name = easygui.enterbox("Hello, what is your name?")
easygui.msgbox(f"Welcome to the Drivers test {name}!")
age = easygui.integerbox(f"How old are you {name}?")
if age < 16:
    easygui.msgbox(f"Sorry {name}, you are not eligable for any drivers licence")
else:
    theory_test = easygui.buttonbox("Have you passed your theory test?", choices=("Yes","No"))
    if theory_test == "No":
        easygui.msgbox("You need to pass your theory test before you attain any licence")
    else:
        if age < 18:
            easygui.msgbox("The highest tier of licence you can attain is Restricted, after you pass the Restricted Practical test")
        else:
            advanced = easygui.buttonbox("Have you passed the Advanced Driving course?", choices = ["Yes","No"])
            if advanced == "Yes":
                if age < 25:
                    easygui.msgbox("You must have your Restricted licence for at least 12 months before applying for your full licence")
                else:
                    easygui.msgbox("You must hold your Restricted licence for at least 3 months before applying for you full licence")
            elif advanced == "no":
                if age < 25:
                    easygui.msgbox("You must have your Restricted licence for at least 18 months before applying for your full licence")
                else:
                    easygui.msgbox("You must have your Restricted licence for at least 6 months before applying for your full licence")
            





If you have passed an Advanced Driving Course:

If under 25:

Must have restricted for at least 12 months

Else if 25 or over:

Must have restricted for at least 3 months

If you have not passed the Advanced Driving Course:

If under 25:

Must have restricted for at least 18 months

Else if 25 or over:

Must have restricted for at least 6 months

And must pass the full licence practical test
