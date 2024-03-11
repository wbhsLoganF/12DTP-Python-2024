import easygui
timetable = {
    1:{
        "Period 1": "DTP",
        "Period 2": "PHYE",
        "Period 3": "CHEE",
        "Period 4": "ECOE",
        "Period 5": "ENGA",
        "Period 6": "MASE"
    },
    2: {
        "Period 1": "PHYE",
        "Period 2": "CHEE",
        "Period 3": "ECOE",
        "Period 4": "ENGA",
        "Period 5": "MASE",
        "Period 6": "DTP"
    },
    3:{
        "Period 1": "CHEE",
        "Period 2": "ECOE",
        "Period 3": "ENGA",
        "Period 4": "MASE",
        "Period 5": "DTP",
        "Period 6": "PHYE"
    },
    4:{
        "Period 1": "ECOE",
        "Period 2": "ENGA",
        "Period 3": "MASE",
        "Period 4": "DTP",
        "Period 5": "PHYE",
        "Period 6": "CHEE"
    },
    5:{
        "Period 1": "ENGA",
        "Period 2": "MASE",
        "Period 3": "DTP",
        "Period 4": "PHYE",
        "Period 5": "CHEE",
        "Period 6": "ECOE"
    },
    6: {
        "Period 1": "MASE",
        "Period 2": "DTP",
        "Period 3": "PHYE",
        "Period 4": "CHEE",
        "Period 5": "ECOE",
        "Period 6": "ENGA"
    }
}

output = ""

input = easygui.buttonbox("Do you want to search for a contact or print the whole list?", choices = ["Print whole", "Search"])
if input == "Print whole":
    for period, period_info in timetable.items():
        output += (f"\nDay: {period} \n")
        for key in period_info:
            output += (f"{key}:{period_info[key]}  ")
    easygui.msgbox(output)

#Search option below   

