def write_to_file(file_name, data):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(data)

# Чтение данных из файла
def read_from_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()

def rewrite_file(file_name, user_text):
    with open(file_name, 'a', encoding='utf-8') as file:
        return file.write(user_text)

# Имя файла
filename = 'qwests.txt'

# Данные для записи
data_to_write = "Тод говард \n Джон кармак \n Том Холл Адриан \n Кармак Джон \n Ромеро Лиза Су "

# Запись данных в файл
write_to_file(filename, data_to_write)

# Чтение данных из файла
read_data = read_from_file(filename)

# Вывод прочитанных данных
print(f"Содержимое файла: {read_data}")

# #Дозапись в файл
# new_text = 'это пример дозаписи'
# rew_file = rewrite_file(filename, new_text)
#
# new_read_data = read_from_file(filename)
#
# # Вывод прочитанных данных
# print(f"Содержимое файла: {new_read_data}")


