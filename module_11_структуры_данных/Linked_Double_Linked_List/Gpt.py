class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def search(self, key):
        temp = self.head
        while temp is not None:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def replace(self, old_value, new_value):
        temp = self.head
        while temp is not None:
            if temp.data == old_value:
                temp.data = new_value
                return
            temp = temp.next

def main():
    linked_list = LinkedList()

    # Ввод чисел от пользователя
    numbers = input("Введите числа через пробел: ").split()
    for number in numbers:
        linked_list.append(int(number))

    while True:
        print("\nМеню:")
        print("1. Добавить элемент в список.")
        print("2. Удалить элемент из списка.")
        print("3. Показать содержимое списка.")
        print("4. Проверить есть ли значение в списке.")
        print("5. Заменить значение в списке.")
        print("6. Выйти.")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            value = int(input("Введите значение для добавления: "))
            linked_list.append(value)
        elif choice == '2':
            value = int(input("Введите значение для удаления: "))
            linked_list.delete(value)
        elif choice == '3':
            linked_list.display()
        elif choice == '4':
            value = int(input("Введите значение для проверки: "))
            if linked_list.search(value):
                print(f"Значение {value} найдено в списке.")
            else:
                print(f"Значение {value} не найдено в списке.")
        elif choice == '5':
            old_value = int(input("Введите значение, которое хотите заменить: "))
            new_value = int(input("Введите новое значение: "))
            linked_list.replace(old_value, new_value)
        elif choice == '6':
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()


