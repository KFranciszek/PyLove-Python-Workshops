# Create a constructor (__init__) for a class "Human", which will take a name, height and weight.


class Human:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight


human = Human("John", "175", "70")
print(human.name)