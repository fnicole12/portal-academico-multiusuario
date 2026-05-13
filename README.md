# Portal Académico Multiusuario

Aplicación web desarrollada con Flask y PostgreSQL para la gestión académica y comunicación escolar.

El sistema permite autenticación de usuarios y acceso diferenciado según rol:
- Administrador
- Profesor
- Alumno
- Padre de familia

---

# Tecnologías utilizadas

- Python
- Flask
- PostgreSQL
- psycopg2
- HTML
- CSS

---

# Funcionalidades actuales

- Login de usuarios
- Validación segura de contraseñas
- Manejo de sesiones
- Control básico por roles
- Dashboard dinámico según rol

---

# Requisitos

Antes de ejecutar el proyecto necesitas:

- Python 3 instalado
- PostgreSQL instalado y ejecutándose
- Git (opcional)

---

# Instalación

## 1. Clonar repositorio

```bash
git clone URL_DEL_REPOSITORIO
cd portal-academico
```

---

## 2. Crear entorno virtual

### Windows

```bash
python -m venv venv
```

Activar entorno virtual:

```bash
venv\Scripts\activate
```

---

## 3. Instalar dependencias

```bash
pip install flask
pip install psycopg2
pip install python-dotenv
pip install werkzeug
```

---

# Configuración de Base de Datos

## 1. Crear base de datos en PostgreSQL

Crear una base llamada:

```text
flask_db
```

---

## 2. Configurar variables de entorno

Crear archivo `.env`

```env
DB_USERNAME=tu_usuario_postgres
DB_PASSWORD=tu_password_postgres
SECRET_KEY=clave_secreta
```

---

## 3. Inicializar base de datos

Ejecutar:

```bash
python init_db.py
```

Esto creará:
- tablas
- relaciones
- datos de prueba

---

# Ejecutar aplicación

```bash
python app.py
```

Abrir navegador en:

```text
http://127.0.0.1:5000/login
```

---

# Usuarios de prueba

## Administrador

```text
Usuario: admin1
Contraseña: 1234
```

## Profesor

```text
Usuario: prof1
Contraseña: 1234
```

## Alumno

```text
Usuario: alum1
Contraseña: 1234
```

## Padre

```text
Usuario: padre1
Contraseña: 1234
```