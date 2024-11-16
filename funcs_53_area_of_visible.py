

def number_of_str():
    str_counter = 0
    elements = ['Новелла', "Роман", "Пьеса", 564, [45], 'ssdfsdf']

    def count_number_of_elements():
        nonlocal str_counter
        for elem in elements:
            if type(elem) is str:
                str_counter +=1
        return f"количество элементов в строке {str_counter}"
    return count_number_of_elements()

number_of_elements = number_of_str()
print(number_of_str())
print(f'счетчик {number_of_elements}')
print(number_of_str())
print(f'счетчик {number_of_elements}')




