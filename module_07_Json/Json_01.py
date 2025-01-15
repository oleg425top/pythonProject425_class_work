import json
'''Код Gpt'''
#Python-объект (словарь)
data = {
    "name": "Иван",
    "age": 30,
    "is_student": False,
    "courses": ["математика", "физика"],
    "address": {
        "city": "Москва",
        "postal_code": "101000"
    }
}

# Преобразование в строку JSON
json_string = json.dumps(data, ensure_ascii=False, indent=4)
print("JSON строка:")
print(json_string)

# Преобразование обратно в Python-объект
parsed_data = json.loads(json_string)
print("\nПарсинг JSON обратно в объект:")
print(parsed_data)



