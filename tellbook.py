#!/usr/bin/env python3
import os
import json
from pathlib import Path
from packages.contact_function import display_menu, add_contact, remove_contact, update_contact, find_contact, contact_list


path = Path("contacts.json")
if path.exists() and type(list(path.read_text()) == list):
    contacts = json.loads(path.read_text())
else:
    contacts = []

while True:
    os.system("clear")
    display_menu(contacts)
    print()
    option = input("Select an option: ")
    if option == "1":
        add_contact(contacts, path)
        pass
    elif option == "2":
        remove_contact(contacts, path)
    elif option == "3":
        update_contact(contacts, path)
    elif option == "4":
        find_contact(contacts)
    elif option == "5":
        contact_list(contacts)
    elif option == "6":
        break

os.system("clear")
