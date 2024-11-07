import random

def get_random_genre(category, categories_matrix):
    if category == 'кино':
        return random.choice(categories_matrix[0])
    elif category == 'книги':
        return random.choice(categories_matrix[1])
    elif category == 'игры':
        return random.choice(categories_matrix[2])
    else:
        return f'{category} -- Не знаю такой категории'

cinema_genres = ["Драма", "Комедия", "Фэнтэзи", "Ужасы"]
book_genres = ["Поэма", "Водевиль", "Роман", "Проза"]
game_genres = ["Симулятор", "Аркада", "RPG", "Инди"]
my_categories_matrix = [cinema_genres,book_genres,game_genres]
print(my_categories_matrix)
user_choice = input('введите жанр: ').lower()
print(get_random_genre(user_choice,my_categories_matrix))







