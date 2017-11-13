# 2.6 Save a file sw_all_heros with heroes in sentences: <name> wazy <mass> kg jest <gender> i pochodzi z <homeworld>
#  Example: Anakin Skywalker wazy 90 kg jest mezczyzna i pochodzi z Tatooine.
# I don't understand why, but there occurrs a KeyError for a key "homeworld".
# "homeworld" is in the JSON file and other keys are read correctly.
import json


with open("py1.2.json") as file:
    data = json.load(file)
sw_all_heros = open("sw_all_heros.txt", "a")
for dictionary in data:
    name = dictionary["name"]
    gender = dictionary["gender"]
    mass = dictionary["mass"]
    if "homeworld" in dictionary:
        homeworld = dictionary["homeworld"]
        sw_all_heros.write(name + " " + " wazy " + mass + " kg jest " + gender + " i pochodzi z " + homeworld + '\n')
    else:
        sw_all_heros.write(name + " " + " wazy " + mass + " kg jest " + gender + " i pochodzi z "
                           + "<KeyError about homeworld>\n")
sw_all_heros.close()
