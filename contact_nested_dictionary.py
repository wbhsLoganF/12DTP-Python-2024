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

for contact_id, contact_info in contacts.items():
    print(f"\ncontact_id: {contact_id}")
    for key in contact_info:
        print(f"{key}: {contact_info[key]}")