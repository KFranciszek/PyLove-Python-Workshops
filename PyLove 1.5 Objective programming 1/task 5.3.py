# Write a function, which will count BMI of "Human" (count_bmi)


class Human:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def count_bmi(self):
        bmi = float(self.weight) / ((float(self.height) / 100)**2)
        print(str(bmi))


human = Human("John", "175", "70")
human.count_bmi()