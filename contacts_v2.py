import easygui
contacts = {
    1:{
        "First Name": "John",
        "Last Name": "Doe",
        "Mobile": "0246810",
        "Email": "john.doe@gmail.com"
    },
    2: {
        "First Name": "Will",
        "Last Name": "Yang",
        "Mobile": "021696120",
        "Email": "bokchoy@gmail.com"
    }
}
p_id = ""
input = easygui.buttonbox("Do you want to search for a contact or print the whole list?", choices = ["Print whole", "Search"])
if input == "Print whole":
    for p_id, contact_info in contacts.items():
        easygui.msgbox(f"\nContact_id: {p_id}")
        for key in contact_info:
            easygui.msgbox(f"{key}: {contact_info[key]}")

#Search option below            
else:
    search = easygui.enterbox("Enter a first name", title = "Enter first name")

    for i in contacts:
        if search in contacts[i]["First Name"] or search in contacts [i]["Last Name"]:
            p_id = contacts[i]
            easygui.msgbox(contacts[i])
        if p_id:
            for key in p_id:
                easygui.msgbox(f"{key}: {p_id[key]}")
        else: 
            easygui.msgbox("Not in contacts")
       
        




