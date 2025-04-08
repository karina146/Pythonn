import json
import csv

def json_to_csv(json_filename):

    with open(json_filename, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    root_key = next(iter(data))
    records = data[root_key]


    csv_filename = f"{root_key}.csv"
    with open(csv_filename, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=records[0].keys())
        writer.writeheader()
        writer.writerows(records)

    print(f"CSV файл '{csv_filename}' успешно создан.")

json_to_csv()
