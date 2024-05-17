import re
import os

choice=""
contacts={}

def add_contact(contacts):

    def is_valid_email(email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    print("Please enter the contact information:")
    while True:
        email_address = input("Enter email address: ")
        if is_valid_email(email_address):
            break
        else:
            print("Please enter a valid email address")

    name = input("Enter the name: ")
    phone_number = input("Enter phone number: ")
    additional_info = input("Enter any additional information: ")

    new_contact = {
        "Name": name,
        "Phone number": phone_number,
        "Additional information": additional_info
    }
    contacts[email_address] = new_contact
    print("Contact added successfully!")
    return contacts



def print_contacts(contacts):
    print("contacts:")
    for email, contact_info in contacts.items():
        print(f"Email: {email}")
        for key, value in contact_info.items():
            print(f"{key}: {value}")
        print()

def edit_contact(contacts):
    try:
        email_to_edit = input("Enter the email address of the contact to edit: ")
        if email_to_edit not in contacts:
            print("Contact not found.")
            return contacts

        print("Current contact information:")
        print(f"Email: {email_to_edit}")
        print("Name:", contacts[email_to_edit]["Name"])
        print("Phone number:", contacts[email_to_edit]["Phone number"])
        print("Additional information:", contacts[email_to_edit]["Additional information"])

        print("Enter new contact information (leave empty to keep current):")
        new_name = input("Enter new name: ")
        new_phone_number = input("Enter new phone number: ")
        new_additional_info = input("Enter new additional information: ")

        if new_name:
            contacts[email_to_edit]["Name"] = new_name
        if new_phone_number:
            contacts[email_to_edit]["Phone number"] = new_phone_number
        if new_additional_info:
            contacts[email_to_edit]["Additional information"] = new_additional_info
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("Contact updated successfully!")
    finally:
        return contacts

def delete_contact(contacts):
    try:
        email_to_delete = input("Enter the email address of the contact to delete: ")
        if email_to_delete not in contacts:
            raise ValueError("Contact not found.")

        del contacts[email_to_delete]
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("Contact deleted successfully!")
    finally:
        return contacts


def search_contact(contacts):
    try:
        email_to_search = input("Enter the email address of the contact to search: ")
        if email_to_search not in contacts:
            raise ValueError("Contact not found.")

        print("Contact details:")
        print(f"Email: {email_to_search}")
        for key, value in contacts[email_to_search].items():
            print(f"{key}: {value}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
def export_contacts(contacts):

    filename = "contacts.txt"
    try:
        with open(filename, "w") as file:
            for email, contact_info in contacts.items():
                file.write(f"Email: {email}\n")
                for key, value in contact_info.items():
                    file.write(f"{key}: {value}\n")
                file.write("\n")
        print(f"Contacts exported to {filename} successfully!")
    except Exception as e:
        print(f"An error occurred while exporting contacts: {e}")

def import_contacts(contacts):

    filename = "contacts.txt"
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            current_email = None
            current_contact = {}
            for line in lines:
                line = line.strip()
                if line.startswith("Email: "):
                    if current_email is not None:
                        contacts[current_email] = current_contact
                    current_email = line[len("Email: "):]
                    current_contact = {}
                elif line: 
                    try:
                        key, value = line.split(": ", 1)
                        current_contact[key] = value
                    except ValueError:
                        print(f"Ignoring invalid line: {line}")
            if current_email is not None:
                contacts[current_email] = current_contact
        print(f"Contacts imported from {filename} successfully!")
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except Exception as e:
        print(f"An error occurred while importing contacts: {e}")

    return contacts

while True:
    print(
        '''
    Welcome to the Contact Management System!
    please select one of the following :
    1-Add a new contact
    2-Edit an existing contact
    3-Delete a contact
    4-Search for a contact
    5-Display all contacts
    6-Export contacts to a text file
    7-Import contacts from a text file
    8-Quit
    '''
    )

    choice = input("")

    if choice == "1":
       add_contact(contacts)
       
    elif choice == "2":
        edit_contact(contacts)

    elif choice == "3":
        delete_contact(contacts)

    elif choice == "4":
       search_contact(contacts)

    elif choice == "5":
        print_contacts(contacts)

    elif choice == "6":
        export_contacts(contacts)

    elif choice == "7":
        import_contacts(contacts)

    elif choice == "8":
        print("Exiting the Contact Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 8.")