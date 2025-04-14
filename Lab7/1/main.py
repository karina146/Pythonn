import json
import jsonschema


with open("error.json", "r") as f:
    data = json.load(f)


with open("schema.json", "r") as f:
    schema = json.load(f)


try:
    jsonschema.validate(instance = data, schema = schema)
    print("Файл прошел валидацию.")
    
except jsonschema.ValidationError as err:
    print(f"Файл не прошел валидацию: {err.message}")