from colorama import Fore, Style
from pprint import pprint
def parse_input(user_input) -> list[str]:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args:list[str], contacts: dict) -> str:
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args:list[str], contacts: dict) -> str:
    name, phone = args
    if not contacts.get(name):
        return "Contact is not exist."
    contacts[name] = phone
    return "Contact added."

def show_phone(args:list[str], contacts: dict) -> str:
    name = args[0]
    contact = contacts.get(name)
    if not contact:
        return "Contact is not exist."
    return contact

def show_all(contacts: dict) -> dict[str, str]:
    return contacts

# colorized command
def print_bot_answer(answer) -> None:
    print(Fore.GREEN + answer + Style.RESET_ALL)

# colorized command
def print_bot_invalid_command(answer: str) -> None:
    print(Fore.RED + answer + Style.RESET_ALL)

def main():
    contacts = {}
    print_bot_answer("Welcome to the assistant bot!")
    while True:
        try:
            print(Style.RESET_ALL + Fore.CYAN + "Enter a command: ", end='')
            user_input = input(Style.RESET_ALL + Fore.YELLOW)

            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print_bot_answer("Good bye!")
                break
            elif command == "hello":
                print_bot_answer("How can I help you?")
            elif command == "add":
                print_bot_answer(add_contact(args, contacts))
            elif command == "change":
                print_bot_answer(change_contact(args, contacts))
            elif command == "phone":
                print_bot_answer(show_phone(args, contacts))
            elif command == "all":
                for name, phone in contacts.items():
                    print_bot_answer(f"{name}: {phone}")
            else:
                print_bot_invalid_command("Invalid command." + Style.RESET_ALL)
        except:
            print_bot_invalid_command("Invalid command.")

if __name__ == "__main__":
    main()
