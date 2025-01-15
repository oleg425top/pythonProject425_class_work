"""O - Open/Closed Principle (Принцип открытости/закрытости):"""


class Employee:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class EmployeeSurname(Employee):
    def __init__(self, name, surname):
        super().__init__(name)
        self.__surname = surname

    def get_surname(self):
        return self.__surname

class TimeSheetReport:

    @staticmethod
    def print_time_sheed(employee_obj):

        try:
            employee_obj.get_surname()
            return f'Сотрудник {employee_obj.get_name()} {employee_obj.get_surname}, печатает отчет'

        except AttributeError:
            return f'Сотрудник {employee_obj.get_name()}, печатает отчет'

employee =Employee("Vasya")
print(TimeSheetReport.print_time_sheed(employee))
employee =EmployeeSurname("Vasya", "Petrov")

