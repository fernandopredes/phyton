from flask import Flask, request, send_from_directory, render_template
from sqlalchemy.exc import IntegrityError

from model import Session, Produto
from model.comentario import Comentario

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html'), 200

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/x-icon')

