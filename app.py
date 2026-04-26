import os
import psycopg2
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='flask_db',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn


@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        # prueba simple
        cur.execute('SELECT 1;')
        result = cur.fetchone()

        cur.close()
        conn.close()

        return f"Conexión exitosa: {result}"

    except Exception as e:
        return f"Error de conexión: {e}"







if __name__ == '__main__':
    app.run(debug=True)