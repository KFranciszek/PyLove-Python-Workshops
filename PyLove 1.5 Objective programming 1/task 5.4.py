# Write a function which will count, how many kg are missing to the norm (diff_to_norm)


class Human:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
        self.bmi = self.count_bmi(

    def count_bmi(self):
        bmi = float(self.weight) / ((float(self.height) / 100)**2)
        return bmi

    def diff_to_norm(self):
        diff = 0
        if self.bmi < 18.5:
            diff = (18.5 - self.bmi) * ((float(self.height) / 100) ** 2)
        elif self.bmi > 24.9:
            diff = (self.bmi - 24.9) * ((float(self.height) / 100) ** 2)
        return diff


human = Human("John", "175", "50")
print(str(human.diff_to_norm()))