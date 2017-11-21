'''Let's imagine a class "Human" with a method "speak" and subclass of "Human" - "Politician" with methods
"receive_bribe" and "lie". Default "Human" after doing method "speak" will print "I tell the truth", but every instance of
"Politician" will say: "I lie, because I can", unless there was executed a method "receive_bribe" earlier, then
he will tell the truth'''


class Human:
    def speak(self):
        print("I tell the truth")


class Politician(Human):

    def __init__(self):
        self.__bribed__ = False

    def receive_bribe(self):
        self.__bribed__ = True

    def speak(self):
        if self.__bribed__:
            print("I tell the truth")
        else:
            print("I lie, because I can")


politician = Politician()
politician.speak()
politician.receive_bribe()
politician.speak()