hero_0 = {
    "name":"Mr Douglass",
    "power":"Transparency",
    "strength":7,
    "speed": 4
    }

hero_1 = {
    "name": "John",
    "power": "Flight",
    "strength": 6,
    "speed": 2 
    }

heroes = [hero_0, hero_1]
#print(f"{heroes}")

for hero_info in heroes:
    print(f"{hero_info['name']}'s power is {hero_info['power']}, their strength value is {hero_info['strength']}, and their speed is {hero_info['speed']}.")