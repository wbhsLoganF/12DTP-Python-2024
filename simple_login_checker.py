import easygui
credentials = {
    "LDO":"1234",
    "SOB":"2345",
    "DCO":"3456",
    "DHA":"4567"
}

username = easygui.enterbox("Enter a username", title = "Enter username")
username = username.upper()

if username in credentials:
    easygui.msgbox("Correct username")
    password = easygui.enterbox("Enter your password", title = "Enter password")
    if password == credentials[username]:
        easygui.msgbox("Access Granted")
    else:
        easygui.msgbox("Access Denied")
else:
    easygui.msgbox("Access Denied")