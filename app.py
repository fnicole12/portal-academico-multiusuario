import os
import psycopg2
from flask import Flask, render_template, request, redirect, url_for, session
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']

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


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        user_id = request.form['user_id']
        password = request.form['password']

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute('''
            SELECT id, user_id, password_hash, role
            FROM users
            WHERE user_id = %s
        ''', (user_id,))

        user = cur.fetchone()

        cur.close()
        conn.close()

        return str(user)

    return render_template('login.html')





if __name__ == '__main__':
    app.run(debug=True)