# Contact Management App
import logging

class Contact:
    def __init__(self, name, phone_number, email=None):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}, Email: {self.email if self.email else 'Not Provided'}"

class ContactManager:
    def __init__(self):
        self.contacts = {}
        logging.basicConfig(level=logging.INFO)

    def add_contact(self, name, phone, email):
        if name in self.contacts:
            logging.info(f"Contact with name {name} already exists.")
        else:
            self.contacts[name] = {"phone": phone, "email": email}
            logging.info(f"Contact {name} added successfully.")

    def view_contacts(self):
        if not self.contacts:
            logging.info("No contacts available.")
        else:
            for name, info in self.contacts.items():
                logging.info(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

    def search_contact(self, name):
        if name in self.contacts:
            info = self.contacts[name]
            logging.info(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
        else:
            logging.info(f"No contact found with name {name}.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            logging.info(f"Contact {name} deleted successfully.")
        else:
            logging.info(f"No contact found with name {name}.")

def main():
    manager = ContactManager()

    while True:
        print("\n--- Contact Management ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email (optional): ")
            manager.add_contact(name, phone_number, email)

        elif choice == "2":
            manager.view_contacts()

        elif choice == "3":
            name = input("Enter name to search: ")
            manager.search_contact(name)

        elif choice == "4":
            name = input("Enter name to delete: ")
            manager.delete_contact(name)

        elif choice == "5":
            print("Exiting the program...")
            break

        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
