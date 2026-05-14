import os
import psycopg2
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash
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

    if 'user_id' in session:
        return redirect(url_for('dashboard'))

    return redirect(url_for('login'))


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

        # validar pwd
        if user and check_password_hash(user[2], password):
            session['user_id'] = user[0]
            session['role'] = user[3]

            return redirect(url_for('dashboard'))

        return render_template(
            'login.html',
            error='Usuario o contraseña incorrecta'
        )

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()

    return redirect(url_for('login'))


########################### ROLES ###########################
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    return render_template(
        'dashboard.html',
        role=session['role']
    )



#ejemplo ruta protegida
@app.route('/nuevo-anuncio')
def nuevo_anuncio():

    if 'user_id' not in session:
        return redirect(url_for('login'))

    if session['role'] != 'admin':
        return '403 - No tienes permiso'

    return 'Formulario nuevo anuncio'


if __name__ == '__main__':
    app.run(debug=True)