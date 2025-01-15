import json

pyton_data = {
    0: "Нулевой",
    1: 1235,
    2: ['item1', 'item2'],
    3: ('item1', 'item2'),
    4: False,
    5: None
}

print(type(pyton_data))
json_data = json.dumps(pyton_data, ensure_ascii=False, indent=4)
print(json_data)
print(type(json_data))

with open('my_json.json', 'w', encoding='utf-8') as file:
    file.write(json_data)