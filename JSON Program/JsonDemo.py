import json
from pprint import pprint

data = json.load(open('Demo.json'))
print(data)
print("---------------------")
print(data["maps"][0]["id"])
print("---------------------")
print(data["maps"][1]["id"])
print("---------------------")
print(data["om_points"])
print("---------------------")
print(data["masks"]["id"])
