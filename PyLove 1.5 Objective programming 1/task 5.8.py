# Write a function, which will advice, wheter it is needed to lose or put on weight (and how much),
# using previous functions (what_to_do)


class Human:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
        self.bmi = self.count_bmi()
        self.diff = self.diff_to_norm()

    def what_to_do(self):
        if self.diff > 0:
            print("Your weight is too big. (" + str(self.diff) + " kg)")
            self.to_burn()
        elif self.diff < 0:
            print("You need to put on weight (" + str(self.diff * (-1)) + " kg)")
            self.to_eat()
        else:
            print("Your weight is okay. You are in norm!")

    def to_burn(self):
        if self.diff > 0:
            kcal_to_burn = float(self.diff * 6000)
            running = kcal_to_burn / 500
            bike = kcal_to_burn / 600
            hobby = kcal_to_burn / 250
            chess = kcal_to_burn / 150
            result = "You should do one of these activities to be in norm: \n"
            result += ("Running: " + str(running) + "h \n")
            result += ("Riding a bike: " + str(bike) + "h \n")
            result += ("Doing hobby: " + str(hobby) + "h \n")
            result += ("Playing chess: " + str(chess) + "h \n")
            print(result)

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


human = Human("John", 175, 65)
human.what_to_do()