#!/usr/bin/env python3
import os
from pathlib import Path

contacts = {}


class Contact:
    def __init__(self, number, firstname, lastname, address):
        self.number = number
        self.firstname = firstname
        self.lastname = lastname
        self.address = address


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


while True:
    os.system("clear")
    display_menu()
    print()
    option = input("Select an option: ")
    if option == "1":
        add_contact()
    elif option == "2":
        pass
    elif option == "3":
        pass
    elif option == "4":
        pass
    elif option == "5":
        pass
    elif option == "6":
        break
