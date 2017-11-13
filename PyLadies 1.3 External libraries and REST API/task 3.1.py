# Change status using an API from http://py.net/ (/status/set) and check if you succeeded (/status)
import requests


resp = requests.get("http://py.net/status")
print(resp.json())
resp = requests.post("http://py.net/status/set", json = { "status": "I like tea"})
print(resp.json())
resp = requests.get("http://py.net/status")
print(resp.json())