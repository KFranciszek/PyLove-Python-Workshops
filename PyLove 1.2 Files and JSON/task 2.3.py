# This task is not finished


def get_data_and_prepare_a_file():
    dictionary = {}
    file = open("py1.2.txt")
    helper_file = open("helper_file.txt", "a")
    while True:
        line = file.readline()
        if line == "":
            break
        else:
            record = line.split(" ")
            if record[2] == "has" and record[4] != "and":
                dictionary[record[1]] = {"height": int(record[7]), "eyes": [record[3], record[4]]}
                helper_file.writelines(record[3][:-1] + " " + record[7] + '\n')
                helper_file.write(record[4] + " " + record[7] + '\n')
            elif record[2] == "has":
                dictionary[record[1]] = {"height": int(record[6]), "eyes": record[3]}
                helper_file.write(record[3] + " " + record[6] + '\n')
            elif record[3] == "has":
                dictionary[record[1] + ' ' + record[2]] = {"height": int(record[7]), "eyes": record[4]}
                helper_file.write(record[4] + " " + record[7] + '\n')
            else:
                dictionary[record[1] + ' ' + record[2] + ' ' + record[3]] = {"height": int(record[8]), "eyes": record[5]}
                helper_file.write(record[5] + " " + record[8] + '\n')

    file.close()
    helper_file.close()


# get_data_and_prepare_a_file()

helper_file = open("helper_file.txt", "r")
new_dictionary = {}
for line in helper_file:
    record = helper_file.readline()
    list = record.split(" ")
    new_dictionary[list[0]] = [0, 0]
helper_file.close()

helper_file = open("helper_file.txt", "r")
for line in helper_file:
    record = helper_file.readline()
    list = record.split(" ")
    new_dictionary[list[0]][0] += float(record[1])
    new_dictionary[list[0]][1] += 1
helper_file.close()


final_file = open("task1.3answer.txt","a")
for key in new_dictionary:
    average = new_dictionary[key][0] / new_dictionary[key][1]
    final_file.write("Średni wzrost osób z kolorem oczu " + key + " wynosi " + str(average))
final_file.close()