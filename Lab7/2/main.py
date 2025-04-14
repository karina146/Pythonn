import json


result_dict = {}

with open("ex_2.json", "r") as f:
    data = json.load(f)

for i in data:
    name = i["name"]
    phone = i["phoneNumber"]
    result_dict[name] = phone


print(result_dict)