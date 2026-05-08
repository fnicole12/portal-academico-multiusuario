import os
import psycopg2
from werkzeug.security import generate_password_hash
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    host="localhost",
    database="flask_db",
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD']
)

# Open a cursor to perform database operations
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS calificaciones;')
cur.execute('DROP TABLE IF EXISTS alumnos_materias;')
cur.execute('DROP TABLE IF EXISTS anuncios;')
cur.execute('DROP TABLE IF EXISTS materias;')
cur.execute('DROP TABLE IF EXISTS users;')

# USERS
cur.execute('''
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(20) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role VARCHAR(20) NOT NULL,
    nombre TEXT NOT NULL
);
''')

# MATERIAS
cur.execute('''
CREATE TABLE materias (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    profesor_id INT REFERENCES users(id)
);
''')

# ALUMNOS_MATERIAS
cur.execute('''
CREATE TABLE alumnos_materias (
    id SERIAL PRIMARY KEY,
    alumno_id INT REFERENCES users(id),
    materia_id INT REFERENCES materias(id)
);
''')

# CALIFICACIONES
cur.execute('''
CREATE TABLE calificaciones (
    id SERIAL PRIMARY KEY,
    alumno_id INT REFERENCES users(id),
    materia_id INT REFERENCES materias(id),
    calificacion NUMERIC(4,2),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
''')

# ANUNCIOS
cur.execute('''
CREATE TABLE anuncios (
    id SERIAL PRIMARY KEY,
    titulo TEXT NOT NULL,
    contenido TEXT NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    autor_id INT REFERENCES users(id)
);
''')


# mockup data
tmp_pass = generate_password_hash('1234')
# usuarios
cur.execute(f'''
INSERT INTO users (user_id, password_hash, role, nombre)
VALUES
('admin1', '{tmp_pass}', 'admin', 'Administrador'),
('prof1', '{tmp_pass}', 'profesor', 'Profesor Uno'),
('alum1', '{tmp_pass}', 'alumno', 'Alumno Uno'),
('padre1', '{tmp_pass}', 'padre', 'Padre Uno');
''')
# materia
cur.execute('''
INSERT INTO materias (nombre, profesor_id)
VALUES ('Matemáticas', 2);
''')
# alumno en materia
cur.execute('''
INSERT INTO alumnos_materias (alumno_id, materia_id)
VALUES (3, 1);
''')
# calificación
cur.execute('''
INSERT INTO calificaciones (alumno_id, materia_id, calificacion)
VALUES (3, 1, 9.0);
''')
# anuncio
cur.execute('''
INSERT INTO anuncios (titulo, contenido, autor_id)
VALUES ('Bienvenida', 'Inicio de clases', 1);
''')

# commit the transaction and apply the changes to the database
conn.commit()

cur.close()
conn.close()