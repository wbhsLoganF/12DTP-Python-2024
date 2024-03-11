import easygui
movies = {
    "Breaking Bad":{
        "Genre": "Crime drama",
        "Released": "2008-2013",
        "Profits": "$186M USD",
        "Rating": "5/5",
    },
    "Better Call Saul":{
        "Genre": "Crime drama",
        "Released": "2015-2022",
        "Profits": "$200M USD",
        "Rating": "5/5",
    },
    "Avengers: Endgame":{
        "Genre": "Superhero",
        "Released": "2019",
        "Profits": "$890M USD",
        "Rating": "5/5",
    },
    "Elvis":{
        "Genre": "Biopic",
        "Released": "2022",
        "Profits": "$288M USD",
        "Rating": "4/5",
    },
    "Minions the Rise of Gru":{
        "Genre": "Historical documentary",
        "Released": "2022",
        "Profits": "$383M USD",
        "Rating": "6/5",
    },
    "":{
        "Genre": "",
        "Released": "",
        "Profits": "$M USD",
        "Rating": "",
    },
    "":{
        "Genre": "",
        "Released": "",
        "Profits": "$M USD",
        "Rating": "",
    },
    "":{
        "Genre": "",
        "Released": "",
        "Profits": "$M USD",
        "Rating": "",
    },
    "":{
        "Genre": "",
        "Released": "",
        "Profits": "$M USD",
        "Rating": "",
    },
    "":{
        "Genre": "",
        "Released": "",
        "Profits": "$M USD",
        "Rating": "",
    }
}

def print_whole():

    output = ""
    for item, item_info in movies.items():
        output += (f"\nTitle: {item} \n\n")
        for key in item_info:
            output += (f"{key}: {item_info[key]}  \n")
    title = "LIST"
    easygui.msgbox(output, title)


def search_option():

    """Allows the user to search a certain title and displays all 
    aspects inside that title""" 
    output = "" 
    categories = [] 
    title = "SEARCH" 
    msg = "Click on the title you would like displayed" 
    #adding the movie titles from the dictionary to a list
    for titles in movies: 
        categories.append(titles) 
    #Getting the users choice
    search_title = easygui.buttonbox(msg, title, categories) 
    for items in movies[search_title]: 
        output += f"\n{items}: {movies[search_title][items]}" 
    title = f"{search_title}"
    easygui.msgbox(output, title) 




"""EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
"""
def add_entry():

    """
EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
"""



#Main menu with all options available as a buttonbox
msg = "Please choose an option"
title = "MAIN MENU"
choices = ["Print Whole", "Search", "Add a Title"]
main_menu = easygui.buttonbox(msg,title,choices)

#checking which function to run based off input from main menu
if main_menu == "Print Whole":
    print_whole()
elif main_menu == "Search":
    search_option()
else:
    add_entry()
