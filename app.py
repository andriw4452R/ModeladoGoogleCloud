# Importamos las librerías necesarias de Flask y SQLAlchemy
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from config import Config  # Archivo de configuración separado (buena práctica)

# Creamos la aplicación Flask
app = Flask(__name__)

# Cargamos la configuración desde la clase Config (ej. conexión a la BD)
app.config.from_object(Config)

# Inicializamos la base de datos con SQLAlchemy
db = SQLAlchemy(app)

# Definimos el modelo de datos para las tareas
class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # ID único de cada tarea
    texto = db.Column(db.String(200), nullable=False)  # Texto de la tarea (obligatorio)
    completada = db.Column(db.Boolean, default=False)  # Estado de la tarea (por defecto False)

    # Representación legible de una tarea, útil para depurar
    def __repr__(self):
        return f'<Tarea {self.texto}>'

# Creamos las tablas en la base de datos si no existen aún
with app.app_context():
    db.create_all()

# Ruta principal que muestra todas las tareas
@app.route("/")
def index():
    tareas = Tarea.query.all()  # Obtenemos todas las tareas de la base de datos
    return render_template("index.html", tareas=tareas)  # Mostramos las tareas en el HTML

# Ruta para agregar una nueva tarea mediante POST
@app.route("/agregar", methods=["POST"])
def agregar():
    texto = request.form["texto"].strip()  # Tomamos el texto desde el formulario y quitamos espacios
    if texto:
        nueva_tarea = Tarea(texto=texto)  # Creamos una nueva tarea
        db.session.add(nueva_tarea)       # La agregamos a la sesión de base de datos
        db.session.commit()               # Guardamos los cambios en la base
    return redirect("/")  # Redirigimos al inicio después de agregar

# Ruta para marcar una tarea como completada
@app.route("/completar/<int:id>")
def completar(id):
    tarea = Tarea.query.get_or_404(id)  # Buscamos la tarea por ID o mostramos error 404 si no existe
    tarea.completada = True             # Marcamos como completada
    db.session.commit()                 # Guardamos el cambio
    return redirect("/")                # Redirigimos al inicio

# Ruta para eliminar todas las tareas que ya están completadas
@app.route("/eliminar_completadas")
def eliminar_completadas():
    Tarea.query.filter_by(completada=True).delete()  # Eliminamos todas las tareas completadas
    db.session.commit()  # Guardamos los cambios
    return redirect("/")  # Redirigimos al inicio

# Ejecutamos la aplicación en modo debug si se llama directamente este archivo
if __name__ == "__main__":
    app.run(debug=True)
