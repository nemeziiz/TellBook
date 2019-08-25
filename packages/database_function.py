import json
from pathlib import Path


def save_contact(contacts, path):
    path.write_text(json.dumps(contacts))
