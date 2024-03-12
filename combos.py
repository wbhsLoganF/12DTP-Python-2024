import easygui
combos = {
    "Value":{
        "Beef Burger": 5.69,
        "Fries": 1.00,
        "Fizzy Drink": 1.00,
        "Total": 7.69

    },
    "Cheezy":{
        "Cheeseburger": 6.69,
        "Fries": 1.00,
        "Fizzy Drink": 1.00,
        "Total": 8.69

    },
    "Super":{
        "Cheeseburger": 6.69,
        "Large Fries": 2.00,
        "Smoothie": 2.00,
        "Total": 10.69

    }
}

def print_whole():
    """Displays entire nested dictionary in one msgbox by adding each
    element to an formatted output"""

    output = ""
    for combo, item_info in combos.items():
        output += (f"\nCombo Name: {combo} \n\n")
        for key in item_info:
            output += (f"{key}: ${item_info[key]}  \n")
    title = "LIST"
    easygui.msgbox(output, title)

def search_option():
    """Allows the user to search a certain combo and displays all
    items inside that combo""" 

    output = "" 
    categories = [] 
    title = "SEARCH" 
    msg = "Click on the combo you would like displayed" 
    #adding the movie titles from the dictionary to a list
    for combo_names in combos: 
        categories.append(combo_names) 
    categories.append("Back") 
    #getting the users choice
    search_combo = easygui.buttonbox(msg, title, categories)
    if search_combo != "Back": 
        for items in combos[search_combo]: 
            output += f"\n{items}: ${combos[search_combo][items]}" 
        title = f"{search_combo}"
        easygui.msgbox(output, title) 


def add_combo():
    """Allows the user to add a new combo to the database"""

    #getting all information for the new entry from user
    msg = "Enter the name of the combo"
    combo = easygui.enterbox(msg)

    msg = "Enter the first item in the combo"
    item_1 = easygui.enterbox(msg)
    msg = "Enter the first item's price"
    type(float);item_1_price = easygui.enterbox(msg)
    

    msg = "Enter the second item of the combo"
    item_2 = easygui.enterbox(msg)
    msg = "Enter the second item's price"
    type(float);item_2_price = easygui.enterbox(msg)


    msg ="Enter the third item of the combo"
    item_3 = easygui.enterbox(msg)
    msg = "Enter the third item's price"
    type(float);item_3_price = easygui.enterbox(msg)

    type(float);total = item_3_price + item_2_price + item_1_price
    """
    msg = f"What is the total price for this combo? (${item_1_price} +
              ${item_2_price} + ${item_3_price} individualy)
    total = easygui.enterbox(msg)
    """
    #add the new entry to the combos dictionary
    combos[combo] = {
        item_1:  item_1_price,
        item_2: item_2_price,
        item_3: item_3_price,
        "Total": total,
    }
    msg = f"{combo} has been added to the database."
    title ="COMBO ADDED"
    easygui.msgbox(msg, title)


def delete_combo():
    """Allows the user to remove a combo from the dictionary entirely
    """

    categories = [] 
    title = "SELECT" 
    msg = "Click on the combo you would like to remove" 
    #adding the combos from the dictionary to a list
    for titles in combos: 
        categories.append(titles)
    categories.append("Back") 

    #getting the users choice
    delete_combo = easygui.buttonbox(msg, title, categories) 

    if delete_combo != "Back":
        msg = f"Are you sure you want to delete {delete_combo}?"
        title = "CONFIRM"
        choices = ["Yes","No"]
        confirm = easygui.buttonbox(msg,title,choices)

        #confirming the choice
        if confirm == "Yes":
            del combos[delete_combo]
            msg = "Done!"
            title = "COMPLETE"
            easygui.msgbox(msg,title)
        else:
            msg = "Cancelled."
            title = "CANCEL"
            easygui.msgbox(msg,title)


#main menu with all options available as a buttonbox
while True:
    msg = "Please choose an option"
    title = "MAIN MENU"                                                            
    choices = ["Print Whole", "Search", "Update Combos", "Quit"]
    main_menu = easygui.buttonbox(msg,title,choices)

    #checking which function to run based off input from main menu
    if main_menu == "Print Whole":
        print_whole() 
    elif main_menu == "Search":
        search_option()

    #a seperate menu if the user wishes to change the dictionary,
    #as to not overcrowd the buttonbox
    elif main_menu == "Update Combos":
        msg = "What do you want to do?"
        title = "CHOOSE"
        choices = ["Add a Combo", "Delete a Combo", "Back"]
        mini_menu = easygui.buttonbox(msg,title,choices)
        if mini_menu == "Add a Combo":
            add_combo()
        elif mini_menu == "Delete a Combo":
            delete_combo()
            
    else:
        break

msg = "Goodbye!"
title = "BYE"
easygui.msgbox(msg, title)