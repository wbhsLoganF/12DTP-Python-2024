import easygui

credentials = {
    "LDO":
    {
        "Username":"LDO",
        "Password": "1234"
    },
    "LOUIS":
    {
        "Louis":"louispassword"
    },
    "RILEY":
    {
        "Riley":"rileypassword"
    }
}
username_input = easygui.enterbox("Insert username")
username_input = username_input.upper()
if username_input in credentials:
    easygui.msgbox("Correct username")
    password = easygui.enterbox("Enter your password")
    if password in credentials[username_input]:
        easygui.msgbox("Access Granted")
    else:
        easygui.msgbox("Access Denied")
else:
    easygui.msgbox("Access Denied")