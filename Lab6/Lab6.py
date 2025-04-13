import json

def json_to_csv(json_file):

    data = []
    with open(json_file, 'r') as f:
        json_data = json.load(f)
        name = list(json_data.keys())[0]
        if isinstance(json_data[name], list):
            data = json_data[name]
    csv_file = f"{name}.csv"
    with open(csv_file, 'w') as f:
        headers = data[0].keys()
        f.write(','.join(headers) + '\n')
        for i in data:
            row = ','.join(str(i[key]) for key in headers)
            f.write(f"{row}\n")

    

json_to_csv("ex2.json")
