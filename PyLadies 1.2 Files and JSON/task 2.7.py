# 2.7 Load a JSON file. Create a file containing all the ships in sentences from the most expensive one to the cheapest:
# <name> kosztuje <123> credits
import json


with open("py1.2zd.json") as file:
    data = json.load(file)

list = []
list2 = []
for ship in data:
    credits = ship["cost_in_credits"]
    if credits != "unknown":
        list.append([ship["name"], int(credits)])
    else:
        list2.append([ship["name"], credits])


# bubble sort:
for i in range(0, len(list)):
    for j in range(0, len(list)-1):
            if list[j][1] < list[j+1][1]:
                helper = list[j]
                list[j] = list[j+1]
                list[j+1] = helper
file = open("file.txt", "a")
for ship in list:
    file.write(ship[0] + " kosztuje " + str(ship[1]) + " credits\n")
for ship in list2:
    file.write(ship[0] + " kosztuje " + ship[1] + " credits\n")
file.close()