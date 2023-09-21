from flask import Flask
import psycopg2
import os

app = Flask(__name__)

app.secret_key = 'root'

def get_db_connection():
    conn = psycopg2.connect(
        host='localhost',
        database='authflask',
        user=os.environ['POSTGRES_USER'],
        password=os.environ['POSTGRES_PASSWORD']
    )
    return conn

conn = get_db_connection()

from routes.routes import *

if __name__ == '__main__':
    app.run(debug=True)
