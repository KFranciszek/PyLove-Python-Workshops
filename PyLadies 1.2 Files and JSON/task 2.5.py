# 2.5 Find and save all the names of women to a file sw_women and all the names of men to a file sw_men
import json


with open("py1.2.json") as file:
    data = json.load(file)
sw_men = open("sw_men.txt", "a")
sw_women = open("sw_women.txt", "a")
for dictionary in data:
    name = dictionary["name"]
    gender = dictionary["gender"]
    if gender == "male":
        sw_men.write(name + '\n')
    elif gender == "female":
        sw_women.write(name + '\n')
sw_men.close()
sw_women.close()
