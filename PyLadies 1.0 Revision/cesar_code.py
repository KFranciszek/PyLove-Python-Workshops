def cesar_code(text, shift):
    new_text = ""
    for letter in text:
        number = ord(letter)
        if (number>= 65 and number<=90):
            number += shift
            while(number > 90):
                number = number % 90 + 65 - 1
        elif (number>=97 and number<=122):
            number+=shift
            while(number > 122):
                number = number % 122 + 97 - 1
        new_text += chr(number)
    return new_text

