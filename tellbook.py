#!/usr/bin/env python3
import os
from pathlib import Path

contacts = []


def display_menu():
    print("Welcome to Contact Book")
    print(f"Total Contacts: {len(contacts)}")
    print("----------------------")
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Update Contact")
    print("4. Find Contact")
    print("5. Contact List")
    print("6. Exit")


def add_contact():
    os.system("clear")
    number = input("Number: ")
    if number in contacts:
        input("The number already exists in book, press enter to back menu...")
    else:
        firstname = input("Firstname: ")
        lastname = input("Lastname: ")
        address = input("Address: ")
        contacts[number] = Contact(number, firstname, lastname, address)
        input("Contact created. press enter to back menu...")


def remove_contact():
    os.system("clear")
    number = input("Number: ")
    if number in contacts:
        del contacts[number]
        input("Contact removed. press enter to back menu...")
    else:
        input("The number is not exists in book, press enter to back menu...")


def update_contact():
    os.system("clear")
    number = input("Number: ")
    if number not in contacts:
        input("The number is not exists in book, press enter to back menu...")
    else:
        firstname = input("Firstname: ")
        lastname = input("Lastname: ")
        address = input("Address: ")
        contacts[number] = Contact(number, firstname, lastname, address)
        input("Contact updated. press enter to back menu...")


def find_contact():
    os.system("clear")
    number = input("Number: ")
    if number not in contacts:
        input("The number is not exists in book, press enter to back menu...")
    else:
        print(
            f"{contacts[number].number}: {contacts[number].firstname} {contacts[number].lastname} from {contacts[number].address}")
        input("Press enter to back to menu...")


def contact_list():
    if len(contacts) == 0:
        print("There are no contacts on your book.")
        input("Press enter to back to menu...")
    else:
        for number in contacts:
            print(
                f"{contacts[number].number}: {contacts[number].firstname} {contacts[number].lastname} from {contacts[number].address}")
        input("Press enter to back to menu...")


while True:
    os.system("clear")
    display_menu()
    print()
    option = input("Select an option: ")
    if option == "1":
        add_contact()
    elif option == "2":
        remove_contact()
    elif option == "3":
        update_contact()
    elif option == "4":
        find_contact()
    elif option == "5":
        contact_list()
    elif option == "6":
        break
