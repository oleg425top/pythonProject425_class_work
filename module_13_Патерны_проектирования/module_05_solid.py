""""L - Liskov Substitution Principle (Принцип подстановки Барбары Лисков):"""


class Document:
    def __init__(self, filename, data = None):
        self.filename = filename
        self.data = data

    def open_document(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                self.data = file.read()
                return self.data
        except FileNotFoundError:
            return 'документ не найден'

    def save_document(self, new_data, method):
        if method == 'rewrite':
            method = 'w'
        else:
            method = 'a'
        with open(self.filename, method) as file:
            file.write(new_data)

class ReadOnlyDocument(Document):
    def save_document(self, new_data, method):
        try:
            raise  Exception
        except Exception:
            print('Только для чтения')

ro_document = ReadOnlyDocument('NO_Solid. txt')
ro_document.save_document('new_document', 'rewrite')