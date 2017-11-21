# Changing digits into "#"
def digit_censorship(text):
    if text.isalpha():
        return text
    new_text = text
    for i in range(len(text)):
        if (text[i] == "0"
            or text[i] == "1"
            or text[i] == "2"
            or text[i] == "3"
            or text[i] == "4"
            or text[i] == "5"
            or text[i] == "6"
            or text[i] == "7"
            or text[i] == "8"
            or text[i] == "9"):
                new_text = new_text[:i] + "#" + new_text[i+1:]
    return new_text