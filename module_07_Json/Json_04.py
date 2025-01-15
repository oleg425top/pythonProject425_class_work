import json
def convert_json(lists_1, list_2):
    dict_1 = dict(zip(lists_1, list_2))
    return dict_1

list_1 = ["cat", "dog", "bird", "lizard"]
list_2 = ["кот ", "собака", "птица", "ящерица"]
print(convert_json(list_1, list_2))


json_data = json.dumps(convert_json, ensure_ascii=False, indent=4)
with open('my_json3.json', 'w', encoding='utf-8') as file:
    file.write(json_data)
