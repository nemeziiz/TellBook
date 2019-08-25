import sqlite3
import json
from pathlib import Path


def save_contact(contacts, path):
    path.write_text(json.dumps(contacts))


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
