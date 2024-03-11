import easygui
bakery = {
    "Savouries":{
        "Sausage roll": 3.50,
        "Mince and cheese": 4.00,
        "Chicken kebab": 2.50,
        "Potatoe top": 4.50,
        "Steak and muschroom": 4.00
    },
    "Sweets":{
        "Donut:": 2.50,
        "Eclair": 3.00,
        "Mud cake slice": 3.00,
        "Gingerbread man": 3.00,
        "Willum": 8.00,
    },
    "Sandwiches": {
        "Pulled pork": 3.00,
        "Pulled chicken": 3.00,
        "Pulled steak": 3.00,
        "Pulled mince": 3.00,
        "Pulled mince again": 3.00,
        
    },
    "Drinks":{
        "Fanta": 2.50,
        "2 Fantas": 5.00,
        "3 Fantas": 7.50,
        "4 Fantas": 10.00,
        "5 Fantas": 12.50,
        
    },
    "Miscellaneous": {
        "Tomato sauce": 0.50,
        "Pay an employee for an hour": 24.00,
        "Buy the employee for a year": 50000.00,
        "lease the building": 900.00,
        "Buy the building": 100000.00,
    }
    }
def print_whole():
    output = ""
    for item, item_info in bakery.items():
        output += (f"\n\nCategory: {item} \n\n")
        for key in item_info:
            output += (f"{key}:${item_info[key]}  \n")
    easygui.msgbox(output)

def input_search(): 
    output = "" 
    msg = "Please enter the name of the item you want to search for" 
    title = "ITEM SEARCH" 
    search_item = easygui.enterbox(msg, title) 
    for categories, items in bakery.items(): 
        if search_item in items: 
            output += f"{search_item}: ${items[search_item]}\n" 
    easygui.msgbox(output) 

def category_search():
    output = ""
    msg = "Enter a bakery category"
    categories = []
    for bakery_categories in bakery:
        categories.append(bakery_categories)

    search = easygui.buttonbox(msg, choices = categories)

    for food_category, food_info in bakery.items():
        if search in food_category:
            output += f"{search}:\n"

            for key in food_info:
                output += f"{key}: ${food_info[key]}\n"
    easygui.msgbox(output)

def add_item():
    categories = []
    for bakery_categories in bakery:
        categories.append(bakery_categories)

    msg = "Choose the category you would like to ass an item to"
    title= "CHOOSE"
    category_choice = easygui.buttonbox(msg,title,categories)

    msg = "Enter the name of the item you would like to add"
    title = "ENTER"
    new_item = easygui.enterbox(msg,title,)

    msg = f"Enter the price of this item"
    title = "ENTER"
    new_item_price = easygui.enterbox(msg,title)

    msg = F"Confirm you want to add {new_item} to {category_choice}"
    title = "CONFIRM"
    choices = ["Yes","No"]
    confirmation = easygui.buttonbox(msg,title,choices)
    if confirmation == "Yes":
        bakery[category_choice][new_item] = new_item_price
        print_whole()
    else:
        msg = "Cancelled."
        easygui.msgbox(msg)




def update_item():
    categories = [] 
    bakery_items = [] 
    for bakery_categories in bakery: 
        categories.append(bakery_categories) 
    msg = "Choose the category of the item you would like to edit" 
    title = "CHOOSE CATEGORY" 
    category_choice = easygui.buttonbox(msg, title, categories) 
    for items in bakery[category_choice]: 
        bakery_items.append(items) 
    msg = "Which item do you wish to adjust?"
    title = "CHOOSE ITEM"
    item = easygui.buttonbox(msg,title,bakery_items)
    msg = f"What will the new price of {item} be?"
    title = "ENTER PRICE"
    price = easygui.enterbox(msg,title)
    msg = f"Are you sure you want to change the price of {item} to ${price}?"
    title = "CONFRIM"
    choices = ["Yes","No"]
    confirm = easygui.buttonbox(msg,title,choices)
    if confirm == "Yes":
        bakery[category_choice][item] = price
        msg = "Done!"
        easygui.msgbox(msg)
    else:
        msg = "Cancelled."
        easygui.msgbox(msg)


options = {
    "Search Item": input_search,
    "Search Category": category_search,
    "Whole Menu": print_whole,
    "Add Item": add_item,
    "Update Item": update_item,
    "Leave": "Leave"
}

#Calls a specific function ftom the options dictionary above

msg = "Please choose an option"
title = "MAIN MENU"
choices = []
for x in options:
    choices.append(x)
while True:
    selection = easygui.buttonbox(msg, title, choices)
    if selection ==  "Search Item": 
        input_search()
    elif selection =="Search Category":
        category_search()
    elif selection =="Whole Menu": 
        print_whole()
    elif selection =="Add Item": 
        add_item()
    elif selection =="Update Item": 
        update_item()
    else:
        msg = "Goodbye!"
        title = "BYE"
        easygui.msgbox(msg, title)
        break