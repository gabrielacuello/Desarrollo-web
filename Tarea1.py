from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Escribe el nombre del juego en la barra de direcciones (minecraft o roblox)"

@app.route("/minecraft/")
def minecraft():
    return render_template('minecraft.html')

@app.route("/roblox/")
def roblox():
    return render_template('roblox.html')

@app.route("/")
def hello():
    return "Escribe el nombre del juego en la barra de direcciones"

@app.route("/<game>/")
def info_games(game):
    if game == "Minecraft":
        return "juego indie de ordenador del género sandbox"
    elif game == "Roblox":
        return "plataforma de juegos online y sistema de creación de juegos"
    else:
        return "aún no conozco este juego"

if __name__ == "__main__":
    app.run()