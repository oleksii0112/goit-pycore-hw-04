import re

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    cmd = re.sub(r"[^a-z]","",cmd)
    return cmd, *args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid format! Usage: add [name] [phone]"
    name, phone = args
    if name in contacts:
        return ("This name is already used, change or add some symbols!")
    else:
        contacts[name] = phone
        return "Contact added."
    
def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid format! Usage: add [name] [phone]"
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Contact {name} updated."
    else:
        return f"There is no contact with name {name}.\nIf you want to add - type 'add [name] [number]'"
    
def show_all(contacts):
    return contacts 

def show_phone(name, contacts):
    if name not in contacts:
        return f"{name} isn`t in contacts"
    else:
        phone = contacts[name]
        return f"{name}`s nubmer is {phone}"

def main():
    contacts = {}
    print ("Welcome to the assistant bot! Type 'hello' to continue, 'exit/close' to exit")
    while True:
        user_input = input("Input a command: ")
        exit_cmd = ["exit", "close"]
        command, *args = parse_input(user_input)
        if command in exit_cmd:
           print("Good bye!")
           break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print (add_contact(args, contacts))
        elif command == "change":
            print (change_contact(args, contacts))
        elif command == "all":
            print (show_all(contacts))
        elif command == "phone":
            if len(args) != 1:
                print ("Type only one contact")
            else:
                print (show_phone(args[0], contacts ))
        else:
            print("Invalid command.")    

if __name__ == "__main__":
    main()

    


