from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from flask_jwt_extended import JWTManager
import sqlite3

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'Database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'Qfi-2.0@123'

jwt =JWTManager(app)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
Database = os.path.join(BASE_DIR, 'Database.db')

def get_db():
    db = getattr(g, '_database',None)
    if db is None:
        db = g._database = sqlite3.connect(Database)
    return db


@app.route('/SignUp', methods=['POST'])
def Register():
    
