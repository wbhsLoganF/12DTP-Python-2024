import easygui
movies = {
    "Breaking Bad":{
        "Genre": "Crime drama",
        "Released": "2008-2013",
        "Profits": "$280M USD",
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
        "Profits": "$2.5B USD",
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
        "Profits": "$940M USD",
        "Rating": "6/5",
    },
    "Joker":{
        "Genre": "Crime drama",
        "Released": "2019",
        "Profits": "$1B USD",
        "Rating": "5/5",
    },
    "Indiana Jones: Raiders of the Lost Ark":{
        "Genre": "Action",
        "Released": "1981",
        "Profits": "$354M USD",
        "Rating": "5/5",
    },
    "Prisoners":{
        "Genre": "Crime Drama",
        "Released": "2013",
        "Profits": "$122M USD",
        "Rating": "4/5",
    },
    "The 5th Wave":{
        "Genre": "Science fiction",
        "Released": "2016",
        "Profits": "$100M USD",
        "Rating": "4/5",
    },
    "Slumdog Millionaire":{
        "Genre": "Drama",
        "Released": "2008",
        "Profits": "$377M USD",
        "Rating": "5/5",
    }
}

def print_whole():
    """Displays entire nested dictionary in one msgbox by adding each
    element to an formatted output"""

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

    #getting the users choice
    search_title = easygui.buttonbox(msg, title, categories) 
    for items in movies[search_title]: 
        output += f"\n{items}: {movies[search_title][items]}" 
    title = f"{search_title}"
    easygui.msgbox(output, title) 


def add_entry():
    """Allows the user to add a new title entry to the database"""

    #getting all information for the new entry from user
    msg = "Enter the title of the movie/show:"
    title = easygui.enterbox(msg)
    msg = "Enter the genre of the movie/show:"
    genre = easygui.enterbox(msg)
    msg = "Enter the release year of the movie/show:"
    released = easygui.enterbox(msg)
    msg ="Enter the profits of the movie/show ($'X'M USD):"
    profits = easygui.enterbox(msg)
    msg = "Enter the rating of the movie/show (out of 5):"
    rating = easygui.enterbox(msg)

    #add the new entry to the movies dictionary
    movies[title] = {
        "Genre": genre,
        "Released": released,
        "Profits": f"${profits}M USD",
        "Rating": f"{rating}/5",
    }
    msg = f"{title} has been added to the database."
    title ="Entry Added"
    easygui.msgbox(msg, title)


def change_rating():
    """Allows the user to change the rating of an existing entry in 
    the database"""

    categories = [] 
    title = "SELECT" 
    msg = "Click on the title you would like to be updated" 
    #adding the movie titles from the dictionary to a list
    for titles in movies: 
        categories.append(titles) 

    #getting the users choice of movie
    movie = easygui.buttonbox(msg, title, categories) 

    #getting the users new rating
    msg = f"What rating would you like to give {movie}"
    title = "ENTER NEW RATING"
    rating = easygui.enterbox(msg,title)

    #confirming the change
    msg = f"Confirm the rating change of '{movie}' to {rating}/5?"
    title = "CONFIRM"
    choices = ["Yes","No"]
    confirm = easygui.buttonbox(msg,title,choices)
    
    if confirm == "Yes":
        movies[movie]["Rating"] = f"{rating}/5"
        msg = "Done!"
        easygui.msgbox(msg)
    else:
        msg = "Cancelled."
        easygui.msgbox(msg)


def delete_title():
    """Allows the user to remove a title from the dictionary entirely
    """

    categories = [] 
    title = "SELECT" 
    msg = "Click on the title you would like to remove" 
    #adding the movie titles from the dictionary to a list
    for titles in movies: 
        categories.append(titles) 

    #getting the users choice
    delete_title = easygui.buttonbox(msg, title, categories) 
    msg= f"Are you sure you want to delete {delete_title}?"
    title = "CONFIRM"
    choices = ["Yes","No"]
    confirm = easygui.buttonbox(msg,title,choices)

    #confirming the choice
    if confirm == "Yes":
        del movies[delete_title]
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
    choices = ["Print Whole", "Search", "Update Titles", "Quit"]
    main_menu = easygui.buttonbox(msg,title,choices)

    #checking which function to run based off input from main menu
    if main_menu == "Print Whole":
        print_whole() 
    elif main_menu == "Search":
        search_option()

    #a seperate menu if the user wishes to change the dictionary,
    #as to not overcrowd the buttonbox
    elif main_menu == "Update Titles":
        msg = "What do you want to do?"
        title = "CHOOSE"
        choices = ["Add a Title", "Change a Rating", "Delete a Title", "Back"]
        mini_menu = easygui.buttonbox(msg,title,choices)
        if mini_menu == "Add a Title":
            add_entry()
        elif mini_menu == "Change a Rating":
            change_rating()
        elif mini_menu == "Delete a Title":
            delete_title()
            
    else:
        break

msg = "Goodbye!"
title = "BYE"
easygui.msgbox(msg, title)