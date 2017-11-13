# Using an API from http://py.net/ download and save on your HDD random cat photos (/cat)
import requests


resp = requests.get("http://py.net/cat")
with open("random_cat.jpg", "wb") as file:
    file.write(resp.content)