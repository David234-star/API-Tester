# Neon-API-Tester/utils/storage.py

import json
import os

DATA_FILE = "app_data.json"


def load_data():
    """Loads application data (history, settings) from a JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {"history": [], "settings": {"theme": "Dark"}}
    return {"history": [], "settings": {"theme": "Dark"}}


def save_data(data):
    """Saves application data to a JSON file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)
