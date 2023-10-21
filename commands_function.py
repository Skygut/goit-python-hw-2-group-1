def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as ve:
            return "Give me name and phone please"
        except KeyError as ke:
            return "User not found"
        except IndexError as ie:
            return "Enter user name"
        except Exception as ea:
            return "Please enter right command"

    return inner


@input_error
def parse_input(user_input):
    if len(user_input) == 0:
        raise Exception
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def validate_args(args):
    if len(args) != 2 or not args[1].isdigit():
        return False
    return True


@input_error
def add_contact(args, contacts):
    if not validate_args(args):
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    if not validate_args(args):
        raise ValueError
    name, phone = args
    if name in contacts.keys():
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError


@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise IndexError
    name = args[0]
    if name in contacts:
        phone = contacts[name]
        return phone
    else:
        raise KeyError


# @input_error
# def show_all(args, contacts):
#     if len(args) != 0:
#         raise Exception
#     return contacts


@input_error
def show_all(args, contacts):
    formatted_list = []
    if len(args) != 0:
        raise Exception
    for name, phone in contacts.items():
        formatted_list.append(f"{name}: {phone}")

    return formatted_list
