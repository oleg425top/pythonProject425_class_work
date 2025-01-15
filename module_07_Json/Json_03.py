import json

# with open(r'C:\Users\oleg8\PycharmProjects\module_05_dicts\module_05_part_2\questions.json', 'r', encoding='utf-8') as file:
#     json_data = file.read()
#     python_data = json.loads(json_data)

with open(r'C:\Users\oleg8\PycharmProjects\module_05_dicts\module_05_part_2\questions.json', 'r', encoding='utf-8') as file:
    data_level = json.load(file)
    level_data = data_level[1]["levels"]


questions = data_level[0]["questions"]
words_easy = questions[0]
words_medium = questions[1]
words_hard = questions[2]
print(words_easy)
print(level_data)
print(questions[2])

