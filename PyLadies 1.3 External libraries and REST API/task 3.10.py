# Using an API from https://swapi.co/api/ display all the names of Gungans in the language of Wookiee
import requests


resp = requests.get("http://swapi.co/api/people")
data = []
while True:
    for man in resp.json()["results"]:
        for species_url in man["species"]:
            species = requests.get(species_url)
            if species.json()["name"] == "Gungan":
                man = requests.get(man["url"] + "?format=wookiee")
                data.append(man.json()["whrascwo"])
    if resp.json()["next"] is not None:
        resp = requests.get(resp.json()["next"])
    else:
        break
print(data)