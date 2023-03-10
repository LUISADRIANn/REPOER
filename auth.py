
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from flask_login import login_user, logout_user, login_required, current_user
from __init__ import db


auth = Blueprint('auth', __name__) # creamos un objeto Blueprint que llamamos 'auth'

@auth.route('/login', methods=['GET', 'POST']) # definir la ruta de la página de acceso
def login(): # define login page fucntion
    if request.method=='GET': # isi la petición es un GET devolvemos la página de inicio de sesión
        return render_template('login.html')
    else: # si la petición es POST comprobamos si el usuario existe y con la contraseña correcta
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        user = User.query.filter_by(email=email).first()
       # comprueba si el usuario existe
        # toma la contraseña proporcionada por el usuario, aplícale un hash y compárala con la contraseña hash de la base de datos.
        if not user:
            flash('Datos No Encontrados Registrate Ya!')
            return redirect(url_for('auth.signup'))
        elif not check_password_hash(user.password, password):
            flash('Compruebe sus datos de acceso e inténtelo de nuevo..')
            return redirect(url_for('auth.login')) # si el usuario no existe o la contraseña es incorrecta, recarga la página
        # si la comprobación anterior pasa, entonces sabemos que el usuario tiene las credenciales correctas
        login_user(user, remember=remember)
        return redirect(url_for('main.profile'))

@auth.route('/signup', methods=['GET', 'POST'])# definimos la ruta de inscripción
def signup(): # definir la función de registro
    if request.method=='GET': # Si la petición es GET devolvemos la página de registro y los formularios
        return render_template('signup.html')
    else: # si la petición es POST, entonces comprobamos si el email no existe ya y entonces guardamos los datos
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first() # si devuelve un usuario, el correo electrónico ya existe en la base de datos
        if user: # si se encuentra un usuario, queremos redirigir de nuevo a la página de registro para que el usuario pueda intentarlo de nuevo
            flash('Email address already exists')
            return redirect(url_for('auth.signup'))
        # create a new user with the form data. Hash the password so the plaintext version isn't saved.
        new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256')) #
        # crear un nuevo usuario con los datos del formulario. Aplica un hash a la contraseña para que no se guarde la versión en texto plano.
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))

@auth.route('/logout') # definir ruta de cierre de sesión
@login_required
def logout(): #define la función de cierre de sesión
    logout_user()
    return redirect(url_for('main.index'))

@auth.route('/inicio') # definir ruta de cierre de sesión
def inicio(): #define la función de cierre de sesión
    return redirect(url_for('main.profile'))

