class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
class ContactManager:
    def __init__(self):
        self.contacts = {}
    def add_contact(self):
        name = input("Enter contact name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contact = Contact(name, phone_number, email, address)
        self.contacts[name] = contact
        print("Contact added successfully!")
    def view_contacts(self):
        for name, contact in self.contacts.items():
            print(f"Name: {name}, Phone Number: {contact.phone_number}")
    def search_contact(self):
        search_term = input("Enter name or phone number to search: ")
        for name, contact in self.contacts.items():
            if name == search_term or contact.phone_number == search_term:
                print(f"Name: {name}, Phone Number: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")
                return
        print("Contact not found!")
    def update_contact(self):
        name = input("Enter contact name to update: ")
        if name in self.contacts:
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contact = self.contacts[name]
            contact.phone_number = phone_number
            contact.email = email
            contact.address = address
            print("Contact updated successfully!")
        else:
            print("Contact not found!")
    def delete_contact(self):
        name = input("Enter contact name to delete:")
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")
def main():
    contact_manager = ContactManager()
    while True:
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            contact_manager.add_contact()
        elif choice == "2":
            contact_manager.view_contacts()
        elif choice == "3":
            contact_manager.search_contact()
        elif choice == "4":
            contact_manager.update_contact()
        elif choice == "5":
            contact_manager.delete_contact()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()

