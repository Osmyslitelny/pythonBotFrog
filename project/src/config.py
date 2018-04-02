import json

with open('project\\resource\\config\\config.json', 'r') as file:
    CONFIG = json.loads(file.read())