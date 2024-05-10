# Importacion de paquetes, librerias y clases.
from flask import Flask, render_template
from config import config

# Instanciamiento de flask
app = Flask(__name__) # template_folder='templates/'

# --- DEFINICIÓN DE RUTAS ---
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/iniciar-sesion")
def iniciar_sesion():
    return render_template("iniciar_sesion.html")

@app.route("/registrarse")
def registrarse():
    return render_template("registrarse.html")

@app.route("/libros")
def obtener_todos_libros():
    return render_template("catalogo.html")

# Ejecución de la aplicacion
if __name__ == '__main__':
    # Recordar: config es un diccionario (objeto)
    app.config.from_object(config['development'])
    app.run()