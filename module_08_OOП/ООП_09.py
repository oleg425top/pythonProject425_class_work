class Book:
    def __init__(self, title, author):
        self._title = title
        self.__author = author


    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self.__author
    @title.setter
    def title(self, title, access):
        if access == 'Модератор':
            self._title = title
            print(f'название изменено на {title}')
        else:
            print(f'у вас нет прав доступа')
    @author.setter
    def author(self, title):
            self.__author = title
            print(f'название изменено на {title}')


book = Book('Дубровский', 'А.С Пушкин')
# print(book._title)
# print(book.__author)
book.("Тютчев")
# book._title = 'Странный человек'
# book.__author = 'М . Ю Лермонтов'
# print(book._title)
# print(book.__author)