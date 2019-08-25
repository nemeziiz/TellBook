#!/usr/bin/env python3
import os
import json
import sqlite3
from pathlib import Path


def create_database():
    with sqlite3.connect("db.sqlite3") as conn:
        command = """CREATE TABLE "contacts" ("number"	TEXT, "firstname"	TEXT, "lastname"	TEXT, "address"	INTEGER,
        PRIMARY KEY("number") );"""
        cursor = conn.cursor()
        cursor.execute(command)
        conn.commit()


def save_database(number, firstname, lastname, address):
    with sqlite3.connect("db.sqlite3") as conn:
        command = "INSERT INTO contacts VALUES(?, ?, ?, ?)"
        cursor = conn.cursor()
        cursor.execute(command, (number, firstname, lastname, address))
        conn.commit()


def update_database(number, firstname, lastname, address):
    with sqlite3.connect("db.sqlite3") as conn:
        command = """UPDATE contacts SET firstname = ?, lastname = ?, address = ? WHERE number = ? """
        cursor = conn.cursor()
        cursor.execute(command, (firstname, lastname, address, number))
        conn.commit()


def remove_database(number):
    with sqlite3.connect("db.sqlite3") as conn:
        command = """DELETE FROM contacts WHERE number = ? """
        cursor = conn.cursor()
        cursor.execute(command, (number, ))
        conn.commit()


def save_contact():
    path.write_text(json.dumps(contacts))


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


def search_contact(number):
    for contact in contacts:
        if contact.get("number") == number:
            return True
    return False


def add_contact():
    os.system("clear")
    number = input("Number: ")
    if search_contact(number):
        input("The number already exists in book, press enter to back menu...")
    else:
        firstname = input("Firstname: ")
        lastname = input("Lastname: ")
        address = input("Address: ")
        contact = {"number": number, "firstname": firstname,
                   "lastname": lastname, "address": address}
        contacts.append(contact)
        save_contact()
        save_database(number, firstname, lastname, address)
        input("Contact created. press enter to back menu...")


def remove_contact():
    os.system("clear")
    number = input("Number: ")
    if search_contact(number):
        i = 0
        for contact in contacts:
            if contact.get("number") == number:
                del contacts[i]
                save_contact()
                remove_database(number)
                break
            i += 1

        input("Contact removed. press enter to back menu...")
    else:
        input("The number is not exists in book, press enter to back menu...")


def update_contact():
    os.system("clear")
    number = input("Number: ")
    if not search_contact(number):
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
                save_contact()
                update_database(number, firstname, lastname, address)
                break
            i += 1
        input("Contact updated. press enter to back menu...")


def find_contact():
    os.system("clear")
    number = input("Number: ")
    if not search_contact(number):
        input("The number is not exists in book, press enter to back menu...")
    else:
        for contact in contacts:
            if contact.get("number") == number:
                print(
                    f"""{contact["number"]}: {contact["firstname"]} {contact["lastname"]} from {contact["address"]}""")
                break
        input("Press enter to back to menu...")


def contact_list():
    if len(contacts) == 0:
        print("There are no contacts on your book.")
        input("Press enter to back to menu...")
    else:
        for contact in contacts:
            print(
                f"""{contact["number"]}: {contact["firstname"]} {contact["lastname"]} from {contact["address"]}""")
        input("Press enter to back to menu...")


if not Path("db.sqlite3").exists():
    create_database()

with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM contacts"
    contacts = conn.execute(command)
    path = Path("contacts.json")
    data = []
    for contact in contacts:
        data.append({"number": contact[0], "firstname": contact[1],
                     "lastname": contact[2], "address": contact[3]})
    path.write_text(json.dumps(data))

path = Path("contacts.json")
if path.exists():
    contacts = json.loads(path.read_text())
else:
    contacts = []


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
