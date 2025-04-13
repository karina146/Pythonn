import json
import csv

def json_to_csv(json_filename):

    data = []
    with open(json_filename, 'r', encoding = "utf-8") as f:
        json_data = json.load(f)
        name = list(json_data.keys())[0]
        if isinstance(json_data[name], list):
            data = json_data[name]
    csv_filename = f"{name}.csv"
    with open(csv_filename, 'w', encoding = "utf-8") as f:
        headers = data[0].keys()
        f.write(','.join(headers) + '\n')
        for i in data:
            row = ','.join(str(i[key]) for key in headers)
            f.write(f"{row}\n")

    

json_to_csv('ex1.json')
