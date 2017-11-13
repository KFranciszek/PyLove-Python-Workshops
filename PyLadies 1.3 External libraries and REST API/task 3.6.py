# Using an API from http://py.net/ try to use query strings (query_string)
import requests


resp = requests.get("http://py.net/query_string?my_number=1&my_status=HelloWorld!!!")
print(resp.json())