from flask import Flask, render_template, url_for, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'una_clave_secreta_muy_larga_y_dificil_de_adivinar'

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



@app.route("/login")
def login():
    return render_template("login.html")



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
            error = "La contraseña no funciona"
        
        if error != None:
            flash(error)
            return render_template("/formulario.html")
        else: 
            flash(f"¡Registro exitoso para el usuario: {nombre}")
            return render_template("/login.html")
        
@app.route("/inicio_sesion", methods = ["POST"])
def iniciar_sesion():
    if request.method == "POST":
        NumeroCorreo = request.form["Correo electronico"]
        Contraseña = request.form["Contrasena"]  
    error = None
    if error != None:
            flash(error)
            return render_template("/login.html")
    else: 
            flash(f"¡Bienvenido!")
            return render_template("/index.html")


if __name__ == "__main__":
    app.run(debug=True)
