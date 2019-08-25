import os
from .database_function import save_contact


def display_menu(contacts):
    print("Welcome to Contact Book")
    print(f"Total Contacts: {len(contacts)}")
    print("----------------------")
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Update Contact")
    print("4. Find Contact")
    print("5. Contact List")
    print("6. Exit")


def search_contact(number, contacts):
    for contact in contacts:
        if contact.get("number") == number:
            return True
    return False


def add_contact(contacts, path):
    os.system("clear")
    number = input("Number: ")
    if search_contact(number, contacts):
        input("The number already exists in book, press enter to back menu...")
    else:
        firstname = input("Firstname: ")
        lastname = input("Lastname: ")
        address = input("Address: ")
        contact = {"number": number, "firstname": firstname,
                   "lastname": lastname, "address": address}
        contacts.append(contact)
        save_contact(contacts, path)
        # save_database(number, firstname, lastname, address)
        input("Contact created. press enter to back menu...")


def remove_contact(contacts, path):
    os.system("clear")
    number = input("Number: ")
    if search_contact(number, contacts):
        i = 0
        for contact in contacts:
            if contact.get("number") == number:
                del contacts[i]
                save_contact(contacts, path)
                # remove_database(number)
                break
            i += 1

        input("Contact removed. press enter to back menu...")
    else:
        input("The number is not exists in book, press enter to back menu...")


def update_contact(contacts, path):
    os.system("clear")
    number = input("Number: ")
    if not search_contact(number, contacts):
        input("The number is not exists in book, press enter to back menu...")
    else:
        firstname = input("Firstname: ")
        lastname = input("Lastname: ")
        address = input("Address: ")
        i = 0
        for contact in contacts:
            if contact.get("number") == number:
                contacts[i] = {"number": number, "firstname": firstname,
                               "lastname": lastname, "address": address}
                save_contact(contacts, path)
                # update_database(number, firstname, lastname, address)
                break
            i += 1
        input("Contact updated. press enter to back menu...")


def find_contact(contacts):
    os.system("clear")
    number = input("Number: ")
    if not search_contact(number, contacts):
        input("The number is not exists in book, press enter to back menu...")
    else:
        for contact in contacts:
            if contact.get("number") == number:
                print(
                    f"""{contact["number"]}: {contact["firstname"]} {contact["lastname"]} from {contact["address"]}""")
                break
        input("Press enter to back to menu...")


def contact_list(contacts):
    if len(contacts) == 0:
        print("There are no contacts on your book.")
        input("Press enter to back to menu...")
    else:
        for contact in contacts:
            print(
                f"""{contact["number"]}: {contact["firstname"]} {contact["lastname"]} from {contact["address"]}""")
        input("Press enter to back to menu...")
