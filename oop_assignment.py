from colorama import Fore, init  # Importing necessary modules from colorama for colored text
from operator import attrgetter  # Importing attrgetter from operator for sorting

# Initialize colorama for automatic color reset
init(autoreset=True)

# Contact class to define contact objects
class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name  # Name of the contact
        self.phone_number = phone_number  # Phone number of the contact
        self.email = email.lower()  # Email of the contact (converted to lowercase)

# ContactBook class to manage contacts
class ContactBook:
    def __init__(self):
        # Initialize with some sample contacts
        self.contacts = [
            Contact("Alice", "1234567890", "alice@email.com"),
            Contact("Bob", "9876543210", "bob@email.com")
        ]

    # Method to add a new contact
    def add_contact(self):
        name = input(Fore.GREEN + "Enter name: ").capitalize()  # Input for contact name (capitalized)
        phone_number = input(Fore.GREEN + "Enter phone number: ")  # Input for phone number
        email = input(Fore.GREEN + "Enter email: ").lower()  # Input for email (converted to lowercase)
        for contact in self.contacts:
            # Check for duplicate contact (same name, phone number, and email)
            if contact.name == name and contact.phone_number == phone_number and contact.email == email:
                print(Fore.RED + "Duplicate record, cannot be added")  # Display error for duplicate
                return
        new_contact = Contact(name, phone_number, email)  # Create new Contact object
        self.contacts.append(new_contact)  # Add new contact to the list
        print(Fore.GREEN + f"{name} has been added.")  # Confirmation message

    # Method to display all contacts sorted by name
    def display_all_contacts(self):
        if self.contacts:  # If contacts list is not empty
            sorted_contacts = sorted(self.contacts, key=attrgetter('name'))  # Sort contacts by name
            print(Fore.YELLOW + "All Contacts:")
            for contact in sorted_contacts:  # Iterate through sorted contacts
                print(f"Name: {contact.name}\nPhone: {contact.phone_number}\nEmail: {contact.email}\n")
        else:
            print(Fore.RED + "No contacts found.")  # Display message if no contacts found

    # Method to search for a contact by name, phone number, or email
    def search_all_contacts(self):
        search = input(Fore.GREEN + "Enter name, phone number, or email ").capitalize()  # Input for search term (capitalized)
        for contact in self.contacts:
            # Check if search term matches name, phone number, or email of any contact
            if search in contact.name or search in contact.phone_number or search in contact.email:
                print(Fore.GREEN + f"Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")
                break
        else:
            print(Fore.RED + "No contact")  # Display message if no contact found

    # Method to update a contact's information
    def update_all_contacts(self):
        search = input(Fore.GREEN + "Enter name, phone number, or email: ").capitalize()  # Input for search term (capitalized)
        for contact in self.contacts:
            # Check if search term matches name, phone number, or email of any contact
            if search in contact.name or search in contact.phone_number or search in contact.email:
                print(Fore.GREEN + f"Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")
                option = input(Fore.GREEN + "Do you wish to change these fields? Y/N: ").upper()  # Prompt for confirmation
                if option == 'Y':  # If user confirms
                    updated_name = input(Fore.GREEN + "Enter new name: ").capitalize()  # Input for updated name (capitalized)
                    if updated_name.strip() != "":  # Check if name input is not empty
                        contact.name = updated_name  # Update contact's name
                    updated_phone_number = input(Fore.GREEN + "Enter new phone number: ")  # Input for updated phone number
                    if updated_phone_number.strip() != "":  # Check if phone number input is not empty
                        contact.phone_number = updated_phone_number  # Update contact's phone number
                    updated_email = input(Fore.GREEN + "Enter new email: ").lower()  # Input for updated email (converted to lowercase)
                    if updated_email.strip() != "":  # Check if email input is not empty
                        contact.email = updated_email  # Update contact's email
                    print(Fore.GREEN + f"Name is {contact.name}, phone number is {contact.phone_number} and the email is {contact.email}")
                    break  # Exit loop after updating contact
                else:
                    print(Fore.RED + "No changes made.")  # Display message if no changes made
                    break  # Exit loop if no changes requested
        else:
            print(Fore.RED + "No contact found.")  # Display message if no contact found

    # Method to delete a contact
    def delete_all_contacts(self):
        search = input(Fore.GREEN + "Enter name, phone number, or email: ").capitalize()  # Input for search term (capitalized)
        for contact in self.contacts:
            # Check if search term matches name, phone number, or email of any contact
            if search in contact.name or search in contact.phone_number or search in contact.email:
                print(Fore.GREEN + f"Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")
                option = input(Fore.GREEN +"Do you wish to delete this record? Y/N: ").upper()  # Prompt for confirmation
                if option == 'Y':  # If user confirms
                    self.contacts.remove(contact)  # Remove contact from the list
                    print(Fore.GREEN + "Contact has been removed")  # Confirmation message
                    break  # Exit loop after deleting contact
                else:
                    print(Fore.RED + "No changes made.")  # Display message if no changes made
                    break  # Exit loop if no changes requested
        else:
            print(Fore.RED + "No contact found.")  # Display message if no contact found

# Main function to run the ContactBook application
def main():
    contact_book = ContactBook()  # Create an instance of ContactBook

    while True:
        # Display menu options
        print(Fore.YELLOW + "\n--- Contact Book Menu ---")
        print(Fore.GREEN + "1. Add New Contact")
        print("2. Display All Contacts")
        print("3. Search for Contact")
        print("4. Update A Contact")
        print("5. Delete A Contact")
        print(Fore.RED + "0. Exit")

        choice = input(Fore.MAGENTA + "Enter your choice: ")  # Input for user choice

        if choice == "1":
            contact_book.add_contact()  # Call add_contact method
        elif choice == "2":
            contact_book.display_all_contacts()  # Call display_all_contacts method
        elif choice == "3":
            contact_book.search_all_contacts()  # Call search_all_contacts method
        elif choice == "4":
            contact_book.update_all_contacts()  # Call update_all_contacts method
        elif choice == "5":
            contact_book.delete_all_contacts()  # Call delete_all_contacts method
        elif choice == "0":
            # Exit message with Terminator ASCII art
            print(r"""
                       ______
                     <((((((\\\
                     /      . }\\
                     ;--..--._|}
  (\                 '--/\--'  )
   \\                | '-'  :'|
    \\               . -==- .-|
     \\               \.__.'   \--._
     [\\          __.--|       //  _/'--.
     \ \\       .'-._ ('-----'/ __/      \\
      \ \\     /   __>|      | '--.       |
       \ \\   |   \   |     /    /       /
        \ '\\ /     \  |     |  _/       /
         \  \       \ |     | /        /
         \  \      \        /
""")
            print("     ________________")
            print("    /                \\")
            print("   /   Hasta la      \\")
            print("  /      vista,       \\")
            print(" /        baby        \\")
            print("/____________________\\")
            break  # Exit the while loop and end the program
        else:
            print(Fore.RED + "Choice between 1 to 0.")  # Display error for invalid choice

if __name__ == "__main__":
    main()  # Call main function if script is executed directly
