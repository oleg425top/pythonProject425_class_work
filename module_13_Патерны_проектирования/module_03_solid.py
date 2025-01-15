"""S Single Responsibility Principle (Принцип единственной ответственности)"""

# class Employee:
#     def __init__(self, name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     def print_time(self):
#         return f'Сотрудник {self.__name} печатает отчет'

class Employee:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

class TimeSheetReport:

    @staticmethod
    def print_time_sheed(employee_obj):
        return f'Сотрудник {employee_obj.get_name()}, печатает отчет'

employee =Employee("Vasya")

print(TimeSheetReport.print_time_sheed(employee))