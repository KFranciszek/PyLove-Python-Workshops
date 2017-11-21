#Checking if the numbers of x and o in text are equal
def xo_checker(text):
    counter_x = 0
    counter_o = 0
    for letter in text:
        if letter == "x":
            counter_x += 1
        elif letter == "o":
            counter_o += 1
        else:
            return "illegal letters in text"

    if counter_x == counter_o:
        return True
    else:
        return False