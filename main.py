import commands_function
from collections import UserDict


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = commands_function.parse_input(user_input)
        if command in ["close", "exit", "bye", "q"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "phone":
            print(commands_function.show_phone(args, contacts))
        elif command == "all":
            print(commands_function.show_all(args, contacts))
        elif command == "add":
            print(commands_function.add_contact(args, contacts))
        elif command == "change":
            print(commands_function.change_contact(args, contacts))
        else:
            print(f"Invalid command: {command}")


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass
    # реалізація класу

class Phone(Field):
    pass
    # реалізація класу

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # реалізація класу


if __name__ == "__main__":
    main()

    # # Створення нової адресної книги
    # book = AddressBook()

    # # Створення запису для John
    # john_record = Record("John")
    # john_record.add_phone("1234567890")
    # john_record.add_phone("5555555555")

    # # Додавання запису John до адресної книги
    # book.add_record(john_record)

    # # Створення та додавання нового запису для Jane
    # jane_record = Record("Jane")
    # jane_record.add_phone("9876543210")
    # book.add_record(jane_record)

    # # Виведення всіх записів у книзі
    # for name, record in book.data.items():
    #     print(record)

    # # Знаходження та редагування телефону для John
    # john = book.find("John")
    # john.edit_phone("1234567890", "1112223333")

    # print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # # Пошук конкретного телефону у записі John
    # found_phone = john.find_phone("5555555555")
    # print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # # Видалення запису Jane
    # book.delete("Jane")
