# site scripts = https://cdnjs.com
# pip install python-socketio flask-socketio simple-websocket

# Frontent
 # html, css, javascript

# Backend -> lógica de funcionamento por trás do site
 # python

# Framework -> Flask -> criar site

# ambiente virtual -> local no seu computador com instalações esp.

        # Criar o Site

# importe o flask
from flask import Flask, render_template
from flask_socketio import SocketIO, send

# crie o app
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# funcionalidade de enviar msg
@socketio.on("message")
def gerenciar_msg(mensagem):
    send(mensagem, broadcast=True)
    usuario_msg(mensagem)

from tinydb import TinyDB

bd = TinyDB("Mensagens.json") 

def usuario_msg(mensagem):
    bd.insert({"MSG": mensagem})

# criar a 1 pagina = 1 rota

@app.route("/")
def homepage():
    return render_template("index.html")


# roda o nosso app
socketio.run(app, allow_unsafe_werkzeug=True)

# websocket -> tunel
