# Implement saving JSON with data of "Human" on HDD. File <name>.json (save_data).
import json


class Human:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
        self.bmi = self.count_bmi()

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

    def save_data(self):
        data = {"name": self.name, "height": self.height, "weight": self.weight, "bmi": self.bmi}
        with open(self.name + ".json", "w") as file:
            json.dump(data, file)


human = Human("John", 170, 60)
human.save_data()