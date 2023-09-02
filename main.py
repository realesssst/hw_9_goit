class Assistant:
    def __init__(self):
        self.contacts = {}

    def input_error(func):
        def wrapper(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except KeyError:
                return "Enter user name"
            except ValueError:
                return "Give me name and phone please"
            except IndexError:
                return "Invalid command format"

        return wrapper

    @input_error
    def add_contact(self, input_str):
        parts = input_str.split(" ")
        name = parts[1]
        phone = parts[2]
        self.contacts[name] = phone
        return f"Added contact: {name} - {phone}"

    @input_error
    def change_contact(self, input_str):
        parts = input_str.split(" ")
        name = parts[1]
        phone = parts[2]
        if name in self.contacts:
            self.contacts[name] = phone
            return f"Changed contact: {name} - {phone}"
        else:
            return f"Contact {name} not found"

    @input_error
    def show_phone(self, input_str):
        name = input_str.split(" ")[1]
        if name in self.contacts:
            return f"Phone for {name}: {self.contacts[name]}"
        else:
            return f"Contact {name} not found"

    def show_all_contacts(self):
        if not self.contacts:
            return "No contacts found"
        result = "All contacts:\n"
        for name, phone in self.contacts.items():
            result += f"{name} - {phone}\n"
        return result

    def main(self):
        print("How can I help you?")
        while True:
            command = input().lower()
            if command == "hello":
                print("How can I help you?")
            elif command.startswith("add "):
                print(self.add_contact(command))
            elif command.startswith("change "):
                print(self.change_contact(command))
            elif command.startswith("phone "):
                print(self.show_phone(command))
            elif command == "show all":
                print(self.show_all_contacts())
            elif command in ["good bye", "close", "exit"]:
                print("Good bye!")
                break
            else:
                print("Invalid command")

if __name__ == "__main__":
    assistant = Assistant()
    assistant.main()