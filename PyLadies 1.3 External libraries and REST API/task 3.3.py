# Download an API Key (api_key) using an API from http://py.net/ - log in (/auth)
import requests


resp = requests.post("http://py.net/auth", json={"name": "SeriousBusinessman", "password": "SeriousPassword"})
api_key = resp.json()["api_key"]
print("API Key: " + api_key)