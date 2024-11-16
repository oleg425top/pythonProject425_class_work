str_counter = 0

def number_of_str():
    global str_counter
    elements = ['Новелла', "Роман", "Пьеса", 564, [45], 'ssdfsdf']
    for elem in elements:
        if type(elem) is str:
            str_counter +=1
    return f"количество элементов в строке {str_counter}"

print(number_of_str())
print(f'счетчик {str_counter}')
print(number_of_str())
print(f'счетчик {str_counter}')

