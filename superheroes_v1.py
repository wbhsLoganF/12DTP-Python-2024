hero_0 = {
    "name":"Materdon",
    "power": "flight",
    "strength": 5,
    "speed": 7
}

name = input("Who were you looking for? ")
if name == hero_0['name']:
    print(f"{hero_0['name']} is the name of our hero, their power is {hero_0['power']} amd their strength value is {hero_0['strength']}")
else:
    print("Sorry, no such name is in our database")

for i in hero_0:
    print(hero_0[i])
    print

