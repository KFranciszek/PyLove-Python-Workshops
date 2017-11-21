# 2.2 Save all people higher than 200 cm to a file hero_200_plus and the rest to a file hero_short
file = open("py1.2.txt")
file1 = open("hero_200_plus.txt", 'a')
file2 = open("hero_short.txt", 'a')


while True:
    line = file.readline()
    if line == "":
        break
    else:
        record = line.split(" ")
        if record[2] == "has" and record[4] != "and":
            if int(record[7]) > 200:
                file1.write(line)
            else:
                file2.write(line)
        elif record[2] == "has":
            if int(record[6]) > 200:
                file1.write(line)
            else:
                file2.write(line)
        elif record[3] == "has":
            if int(record[7]) > 200:
                file1.write(line)
            else:
                file2.write(line)
        else:
            if int(record[8]) > 200:
                file1.write(line)
            else:
                file2.write(line)

file.close()
file1.close()
file2.close()