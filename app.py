from flask import Flask, render_template, url_for, request, flash, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'una_clave_secreta_muy_larga_y_dificil_de_adivinar'

USUARIOS_REGISTRADOS = {
    'admin@correo.com' :  {
        'password' : 'Admin123',
        'nombre' : 'Administrador',
        'fecha_nacimiento' : '14/05/1998'
}
}

@app.route('/validalogin', methods=['GET', 'POST'])
def validaLogin():
    if request.method == 'POST':
        email=request.form.get('Correo_electronico', '').strip()
        password = request.form.get('Contrasena', '')


@app.route("/")
def form():
    return render_template("formulario.html")
@app.route("/inicio")
def inicio():
    return render_template("index.html")

@app.route("/animales")
def animales():
    return render_template("animales.html")

@app.route("/vehiculos")
def vehiculos():
    return render_template("vehiculos.html")

@app.route("/maravillas")
def maravillas():
    return render_template("maravillas.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/login')
def login():
    if session.get('logueado') ==True:
        session.clear()
        return render_template("index.html")

@app.route("/registrame", methods = ["GET", "POST"])
def registrame():
    error = None
    if request.method == "POST":
        nombre = request.form["Nombre"]
        apellido = request.form["Apellido"]
        dia = request.form["dia"]
        mes = request.form["mes"]
        año = request.form["año"]
        genero = request.form["Género"]
        NumeroCorreo = request.form["NumeroCorreo"]
        Contraseña = request.form["Contraseña"]
        ConfirmarContra = request.form["ConfirmarContra"]
        
        if Contraseña != ConfirmarContra:
            error = "Las contraseñas no coinciden :("
        
        if error != None:
            flash(error)
            return render_template("/formulario.html")
        else: 
            flash(f"¡Registro exitoso para el usuario: {nombre}")
            return render_template("/login.html")
        
@app.route('/login/<username>')
def login_user(username):
    session['username'] = username
    return 'Logged in as ' + username

@app.route('/profile')
def profile():
    username = session.get('username')
    if username is not None:
            return 'User: ' + username
    return 'Not logged in'

@app.route('/logout')
def logout():  
    session.pop('username', None)
    return 'Logged out'

if __name__ == "__main__":
    app.run(debug=True)
