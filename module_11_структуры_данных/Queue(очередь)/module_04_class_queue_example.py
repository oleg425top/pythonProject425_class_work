class PrinterQueue:
    def __init__(self, printer_queue: list = None):
        if printer_queue is None:
            self.__printer_queue = []
        else:
            self.__printer_queue = printer_queue

    def add_document(self, document_name):
        if len(self.__printer_queue) == 0 :
            self.__printer_queue.append(document_name)
            return f'документ: {document_name} в обработке'
        else:
            self.__printer_queue.append(document_name)
            return f'{document_name} - документ в очереди'

    # def print_document(self):
    #     document = self.__printer_queue.pop(0)
    #     return f' Print of {document}'

    def print_documents(self):
        while self.__printer_queue:
            document = self.__printer_queue.pop(0)
            print(f'Печать документа: {document}')
        return 'Очередь печати пуста'

hp_printer = PrinterQueue()

print(hp_printer.add_document('Doc_1'))
print(hp_printer.print_documents())
print()
kyocera_printer = PrinterQueue(['Документ 1', 'Document 2'])
print(kyocera_printer.add_document('Doc_10'))
print(kyocera_printer.add_document('Doc_11'))
print(kyocera_printer.print_documents())



