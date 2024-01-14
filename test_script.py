import json

with open('./output.json', 'r') as output_file:
    for line in output_file:
        x = json.loads(line)
        print(x["keywords"])
