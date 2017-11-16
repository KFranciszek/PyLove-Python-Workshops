def count_vowels(text):
    if text == "":
        return 0
    else:
        sum = 0
        text = text.lower()
        for letter in text:
            if (letter == "a"
                or letter == "e"
                or letter == "i"
                or letter == "o"
                or letter == "u"
                or letter == "y"):
                    sum += 1
        return sum

