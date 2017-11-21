''' Assuming that to lose 1 kg you need to burn 6000 kcal, write a functionality, which will tell
the user how many hours he should run (500kcal/h) / ride a bike (600kcal/h) / do a hobby (250/kcal/h)
/ play chess (150kcal/h) / etc. to be in norm (to_burn) '''


class Human:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
        self.bmi = self.count_bmi()
        self.diff = self.diff_to_norm()

    def to_burn(self):
        if self.diff > 0:
            kcal_to_burn = float(self.diff * 6000)
            running = kcal_to_burn / 500
            bike = kcal_to_burn / 600
            hobby = kcal_to_burn / 250
            chess = kcal_to_burn / 150
            result = ("You should do one of these activities to be in norm: \n")
            result += ("Running: " + str(running) + "h \n")
            result += ("Riding a bike: " + str(bike) + "h \n")
            result += ("Doing hobby: " + str(hobby) + "h \n")
            result += ("Playing chess: " + str(chess) + "h \n")
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


human = Human("John", 175, 90)
human.to_burn()