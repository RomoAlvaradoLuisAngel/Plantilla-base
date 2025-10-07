from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    arr = ["Luis", "Paco", "Rosita", "Martin", "Messi"]
    autor = "Luis Angel Romo Alvarado"
    return render_template("index.html", nombre = autor, amigos = arr)


if __name__ == "__main__":
    app.run(debug=True)