import json

with open("Input.json", "r") as input:
    obj = json.load(input)
    print("Hello, " + obj["name"])
