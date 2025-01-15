class Book:
    def __init__(self, title, author):
        self._title = title
        self.__author = author

    def get_title(self):
        return self._title

    def get_author(self):
        return self.__author

    def set_title(self, title, access):
        if access == 'Модератор':
            self._title = title
            return f'название изменено на {title}'
        else:
            f'у вас нет прав доступа'

    def set_author(self, title, access):
        if access == 'Модератор':
            self.__author = title
            return f'название изменено на {title}'
        else:
            f'у вас нет прав доступа'

book = Book('Дубровский', 'А.С Пушкин')
# print(book._title)
# print(book.__author)
print(book.set_author("Тютчев", 'Модератор'))
# book._title = 'Странный человек'
# book.__author = 'М . Ю Лермонтов'
# print(book._title)
# print(book.__author)