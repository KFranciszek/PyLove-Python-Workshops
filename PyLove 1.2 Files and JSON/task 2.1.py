# 2.1 Load a file and create a dictionary where name (and surname) will be a key and the value will be a dictionary
# with keys of eyes colour and height. Example: {"Yoda": {"height": 66, "eyes": "brown"}}
dictionary = {}
file = open("py1.2.txt")
while True:
    line = file.readline()
    if line == "":
        break
    else:
        record = line.split(" ")
        if record[2] == "has" and record[4] != "and":
            dictionary[record[1]] = {"height": int(record[7]), "eyes": record[3] + record[4]}
        elif record[2] == "has":
            dictionary[record[1]] = {"height": int(record[6]), "eyes": record[3]}
        elif record[3] == "has":
            dictionary[record[1] + ' ' + record[2]] = {"height": int(record[7]), "eyes": record[4]}
        else:
            dictionary[record[1] + ' ' + record[2] + ' ' + record[3]] = {"height": int(record[8]), "eyes": record[5]}
