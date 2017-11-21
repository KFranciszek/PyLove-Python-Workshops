# Set your user status (/user_status/set) after getting API key (api_key) using an API from http://py.net/
# and check others status (/user_status), especially the status of your mate near you
import requests


resp = requests.post("http://py.net/auth", json={"name": "SeriousBusinessman", "password": "SeriousPassword"})
api_key = resp.json()["api_key"]
resp = requests.post("http://py.net/user_status/set",
                     json={"api_key": api_key, "name": "SeriousBusinessman", "password": "SeriousPassword",
                           "status": "Hello world!!!"})
print(resp.json())
resp = requests.get("http://py.net/user_status")
print(resp.json())

