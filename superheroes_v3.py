heroes = {
    "LDO":
    {
        "Name":"Mr Douglass",
        "power":"Transparency",
        "strength":7,
        "speed": 5,
    },
    "JOHN":
    {
        "Name": "John",
        "power": "Flight",
        "strength": 6,
        "speed": 2,
    }
}
for hero_id, hero_info in heroes.items():
    print(f"\nHero ID: {hero_id}")

    for key in hero_info:
        print(f"{key} : {hero_info[key]}")