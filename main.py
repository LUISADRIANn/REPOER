
from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from __init__ import create_app, db
import sqlite3
main = Blueprint('main', __name__)

def conexion():
    conn = sqlite3.connect("PERFIL EMPRESA SA.sqlite")
    conn.row_factory = sqlite3.Row
    return conn



@main.route('/') # página de inicio que devuelve 'index
def index():
    return render_template('index.html')





@main.route('/profile') # página de perfil que devuelve 'perfil
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

app = create_app() # inicializamos nuestra aplicación flask usando la función __init__.py
if __name__ == '__main__':
    with app.app_context():
        db.create_all() # crear la base de datos SQLite
    app.run(debug=True) # ejecuta la aplicación flask en modo debug# ejecuta la aplicación flask en modo debug



@main.route('/AJUSTES') # página  devuelve AJUSTE HTML :)
def AJUSTES():
    return render_template('AJUSTES.html')

@main.route("/CREW") # RETORNO DE TICKETS
def CREW():
    conn = conexion()
    posts = conn.execute("Select * FROM datosest").fetchall()
    return render_template('CREATUTIKECT.html' , posts=posts)

