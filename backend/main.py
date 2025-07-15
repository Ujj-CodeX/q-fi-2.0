from flask import Flask, jsonify, request,g
from flask_cors import CORS
from model import db, User, Course, Subject, Chapter,Question,Option,QuizResult 
import os
from flask_jwt_extended import JWTManager
import sqlite3
import datetime


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
    data = request.json

    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    dob = data.get('dob')  
    gender = data.get('gender')
    course = data.get('course')

   
    if not all([username, password, email, dob, gender, course]):
        return jsonify({'success': False, 'error': 'All fields are required.'}), 400

   
    if User.query.filter_by(username=username).first():
        return jsonify({'success': False, 'error': 'Username already exists.'}), 400
    if User.query.filter_by(email=email).first():
        return jsonify({'success': False, 'error': 'Email already exists.'}), 400

    
    new_user = User(
        username=username,
        password=password,
        email=email,
        dob=dob,
        gender=gender,
        course=course
    )

    
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'success': True, 'message': 'User registered successfully.'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500
    

@app.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return jsonify([{'id': course.id, 'name': course.name} for course in courses])



if __name__ == '__main__':
    app.run(debug=True)