#!/usr/bin/env python3
import os
import json
import sqlite3
from pathlib import Path
from packages.contact_function import display_menu, add_contact, remove_contact, update_contact, find_contact, contact_list
# from database_function import create_database

# if not Path("db.sqlite3").exists():
#     create_database()

path = Path("contacts.json")
if path.exists():
    contacts = json.loads(path.read_text())
else:
    contacts = []

# with sqlite3.connect("db.sqlite3") as conn:
#     command = "SELECT * FROM contacts"
#     contacts = conn.execute(command)
#     data = []
#     path2 = "db.sqlite3"
#     for contact in contacts:
#         data.append({"number": contact[0], "firstname": contact[1],
#                      "lastname": contact[2], "address": contact[3]})
#         path2.write_text(json.dumps(data))


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
