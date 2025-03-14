from typing import List, Dict
from flask import Flask, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)


def favorite_colors() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'knights'
    }

    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute('SELECT name, color FROM favorite_colors')
        results = [{'name': name, 'color': color} for (name, color) in cursor]
    except Error as e:
        print(f"Error: {e}")
        results = []
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    return results


@app.route('/')
def index() -> str:
    colors = favorite_colors()
    return jsonify({'favorite_colors': colors})


if __name__ == '__main__':
    app.run(host='0.0.0.0')

