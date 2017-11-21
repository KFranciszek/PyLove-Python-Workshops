#Counting words in a text
def count_words(text):
    if text == "":
        return 0
    else:
        sum = 1
        for letter in text:
            if letter == " ":
                sum += 1
        return sum