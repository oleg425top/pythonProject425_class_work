class Publication:
    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = year

    def display(self):
        print(f'Название {self.__title}')
        print(f'автор {self.__author}')
        print(f' год {self.__year}')

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_year(self):
        return self.__year

class Book(Publication):
    def __init__(self, title, author, year, code):
        super().__init__(title, author, year)
        self.__code = code

    def display(self):
        super().display()
        print(f'Код книги {self.__code}')

    def get_code(self):
        return self.__code

    def get_book_data(self):
        return f'{self.get_title()}, {self.get_author()}, {self.get_code()}'

    def get_book_data_var(self):
        title = self.get_title()
        author = self.get_author()
        code = self.get_code()
        return f'{title}, {author}, {code}'

    class Magazine(Publication):
        def __init__(self, title, author, year, iisue_number):
            super().__init__(title, author, year, iisue_number)


