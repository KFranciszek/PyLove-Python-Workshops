# Register using an API from http://py.net/ (/register). Remember that there can be only one user under given name (name)
import requests


resp = requests.post("http://py.net/register", json={"name": "SeriousBusinessman", "password": "SeriousPassword"})
print(resp.json())