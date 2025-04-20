import configparser
import json
import sqlite3
from flask import Flask, jsonify
import os

CONFIG_FILE = '/Users/abhijeetchavan/Developer/hero-vired/Assignment_One/config.ini'
DB_FILE = '/Users/abhijeetchavan/Developer/hero-vired/Assignment_One/config.db'

def parse_config(file_path):
    config_data = {}
    config = configparser.ConfigParser()

    if not os.path.exists(file_path):
        raise FileNotFoundError("Configuration file not found.")

    config.read(file_path)

    for section in config.sections():
        config_data[section] = {}
        for key in config[section]:
            config_data[section][key] = config[section][key]

    return config_data

def save_to_database(data, db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS config_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            config_json TEXT
        )
    ''')

    json_data = json.dumps(data)
    cursor.execute('INSERT INTO config_data (config_json) VALUES (?)', (json_data,))
    conn.commit()
    conn.close()

def get_latest_config(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT config_json FROM config_data ORDER BY id DESC LIMIT 1')
    row = cursor.fetchone()
    conn.close()
    if row:
        return json.loads(row[0])
    return {}

# Parse and save once at the start
try:
    config_dict = parse_config(CONFIG_FILE)
    print("Configuration File Parser Results:\n")
    for section, values in config_dict.items():
        print(f"{section}:")
        for key, val in values.items():
            print(f"- {key}: {val}")
    save_to_database(config_dict, DB_FILE)
except Exception as e:
    print(f"Error: {e}")

# Flask app to serve the config
app = Flask(__name__)

@app.route("/config", methods=["GET"])
def get_config():
    try:
        data = get_latest_config(DB_FILE)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)