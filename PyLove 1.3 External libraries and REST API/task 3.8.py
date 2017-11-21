# Using an API from https://swapi.co/api display all names of species occurring in the fifth part of Star Wars
import requests


data = []
resp = requests.get("http://swapi.co/api/species/")
while True:
    for species in resp.json()["results"]:
        for url in species["films"]:
            film = requests.get(url)
            if film.json()["episode_id"] == 5:
                data.append(species)
                if resp.json()["next"] is not None:
                    resp = requests.get(resp.json()["next"])
                else:
                    break
print(data)