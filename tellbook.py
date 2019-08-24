#!/usr/bin/env python3
import os
from pathlib import Path


class Contact:
    def __init__(self, number, firstname, lastname, address):
        self.number = number
        self.firstname = firstname
        self.lastname = lastname
        self.address = address


def display_menu():
    print("Welcome to Contact Book")
    print("----------------------")
    print("1. Add Contact")
    print("3. Update Contact")
    print("4. Find Contact")
    print("5. Contact List")
    print("6. Exit")


while True:
    os.system("clear")
    display_menu()
    print()
    option = input("Select an option: ")
    if option == "1":
        pass
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
