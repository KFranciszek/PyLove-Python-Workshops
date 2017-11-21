# Using an API from https://swapi.co/api get data of all inhabitants of the planet Tatooine
import requests


resp = requests.get("http://swapi.co/api/planets")
residents = []
while True:
    for planet in resp.json()["results"]:
        if planet["name"] == "Tatooine":
            for resident_url in planet["residents"]:
                resident = requests.get(resident_url)
                residents.append(resident.json())
            break
    if resp.json()["next"] is not None and residents == []:
        resp = requests.get(resp.json()["next"])
    else:
        break
print(residents)