# Assuming that to put 1 kg more on weight, you need 6000 kcal, write a functionality, which will tell the user,
# how much of chocolate he should eat (450kcal/100g) / potatoes(80kcal/100g) more to be in norm (to_eat)


class Human:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
        self.bmi = self.count_bmi()
        self.diff = self.diff_to_norm()

    def to_eat(self):
        if self.diff < 0:
            kcal_to_get = float(self.diff * 6000 * (-1))
            chocolate = kcal_to_get / (450*10)
            potatoes = kcal_to_get / (80*10)
            result = ("You should eat one of these products to be in norm: \n")
            result += ("Chocolate: " + str(chocolate) + "kg \n")
            result += ("Potatoes: " + str(potatoes) + "kg \n")
            print(result)

    def count_bmi(self):
        bmi = float(self.weight) / ((float(self.height) / 100)**2)
        return bmi

    def diff_to_norm(self):
        diff = 0
        if self.bmi < 18.5:
            diff = (18.5 - self.bmi) * ((float(self.height) / 100) ** 2) * (-1)
        elif self.bmi > 24.9:
            diff = (self.bmi - 24.9) * ((float(self.height) / 100) ** 2)
        return diff


human = Human("John", 175, 56.5)
human.to_eat()