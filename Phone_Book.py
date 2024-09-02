# Phone book dictionary
phone_book = {}

# Function to add a contact
def add_contact(name, number):
    phone_book[name] = number
    print(f"{name} has been added successfully.")

# Function to search for a contact
def search_contact(name):
    if name in phone_book:
        print(f"The phone number for {name} is: {phone_book[name]}")
    else:
        print(f"{name} is not found in the phone book.")

# Function to delete a contact
def delete_contact(name):
    if name in phone_book:
        del phone_book[name]
        print(f"{name} has been deleted successfully.")
    else:
        print(f"{name} is not found in the phone book.")

# Function to list all contacts
def list_contacts():
    if phone_book:
        for name, number in phone_book.items():
            print(f"{name}: {number}")
    else:
        print("No contacts in the phone book.")

# Main program loop
while True:
    print("\nPhone Book Application")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. List All Contacts")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Name: ")
        number = input("Phone Number: ")
        add_contact(name, number)
    elif choice == '2':
        name = input("Name to search: ")
        search_contact(name)
    elif choice == '3':
        name = input("Name to delete: ")
        delete_contact(name)
    elif choice == '4':
        list_contacts()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again.")


