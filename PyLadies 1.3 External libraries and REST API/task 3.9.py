# Using an API from https://swapi.co/api/ count BMI of all pilots of Millennium Falcon and display them with their names
import requests


resp = requests.get("http://swapi.co/api/starships")
data = []
while True:
    for starship in resp.json()["results"]:
        if starship["name"] == "Millennium Falcon":
            for pilot_url in starship["pilots"]:
                pilot = requests.get(pilot_url)
                pilot = pilot.json()
                bmi = float(pilot["mass"]) / ((int(pilot["height"]) / 100) ** 2)
                data.append(pilot["name"] + " " + str(bmi))
                break
                if data == [] and resp.json()["next"] is not None:
                    resp = requests.get(resp.json()["next"])
                else:
                    break
print(data)