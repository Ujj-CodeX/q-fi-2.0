from flask import Flask, jsonify, request,g
from flask_cors import CORS
from model import db, User, Course, Subject, Chapter,Question,Option,QuizResult ,Review2, QuizRating
import os
from flask_jwt_extended import JWTManager,create_access_token,jwt_required, get_jwt_identity,decode_token,get_jwt
import sqlite3
import datetime
from datetime import timezone,timedelta
from flask import jsonify, request , send_file
from sqlalchemy import func, distinct
import csv
import io
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from werkzeug.security import check_password_hash,generate_password_hash
from flask_jwt_extended import create_access_token
from functools import wraps
from zoneinfo import ZoneInfo



app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'Database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'Qfi-2.0@123'

db.init_app(app)


jwt =JWTManager(app)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
Database = os.path.join(BASE_DIR, 'Database.db')

def get_db():
    db = getattr(g, '_database',None)
    if db is None:
        db = g._database = sqlite3.connect(Database)
    return db

def valid_user(username, course):
    conn = get_db()
    user = conn.execute('SELECT * FROM users WHERE username = ? AND course = ?', 
                        (username, course)).fetchone()
    conn.close()
    return user is not None

##################-- Login Setup ------#########
@app.route('/Admin_login', methods=['POST'])
def admin():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    conn = get_db()
    user = conn.execute('SELECT * FROM admin WHERE username = ?', (username,)).fetchone()
    conn.close()

    if user and check_password_hash(user[2], password):
        identity_data = f"{username}"
        access_token = create_access_token(identity=identity_data)
        return jsonify({"access_token": access_token}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    conn = get_db()
    user = conn.execute('SELECT * FROM user WHERE username = ? ', 
                        (username, )).fetchone()
    conn.close()

    if user and check_password_hash(user[3], password):
        identity_data = f"{username}:{user[7]}"  
        access_token = create_access_token(identity=identity_data)
        return jsonify({"access_token": access_token}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

@app.route('/change-password', methods=['POST'])
def change_password():
    data = request.json
    username = data.get('username')
    new_password = data.get('new_password')

    if not username or not new_password:
        return jsonify({'error': 'Username and password are required.'})

    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Check if the username exists
        cursor.execute('SELECT * FROM user WHERE username = ?', (username,))
        user = cursor.fetchone()

        if user:
            # Hash the new password
            hashed_password = generate_password_hash(new_password)

            # Update the password
            cursor.execute('UPDATE user SET password = ? WHERE username = ?', (hashed_password, username))
            conn.commit()
            conn.close()
            return jsonify({'success': True, 'message': 'Password updated successfully.'})
        else:
            conn.close()
            return jsonify({'error': 'Username not found.'})

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    identity = get_jwt_identity()  
    print(" Protected Route - Token Data:", identity)

    try:
        username, course = identity.split(':') 
    except ValueError:
        return jsonify({"error": "Invalid token format"}), 400

    return jsonify({
        "username": username,
        "course": course
    }), 200


@app.route('/submit_review', methods=['POST'])
def submit_review():
    data = request.json

    username = data.get('username')
    review = data.get('review')

    # Basic validation
    if not username or not review:
        return jsonify({'success': False, 'error': 'Username and review are required.'}), 400

    try:
        new_review = Review2(username=username, review=review)
        db.session.add(new_review)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Review submitted successfully.'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500
############################################################################

####--------------User dashboard------------------#############

@app.route('/subjects1', methods=['GET'])
@jwt_required()
def get_subjects1():
    identity = get_jwt_identity()  
    print("Token Data (identity):", identity)

    try:
        username, course = identity.split(':') 
    except ValueError:
        return jsonify({"error": "Invalid token format"}), 400

    conn = get_db()
    subjects = conn.execute(
        'SELECT s.id AS subject_id , s.name FROM subject s JOIN course c ON s.course_id = c.id WHERE c.name = ?;', 
        (course,)
    ).fetchall()
    conn.close()

    return jsonify([{"subject_id": subject[0], "name": subject[1]} for subject in subjects])

@app.route('/chapters1/<subject_id>', methods=['GET'])
@jwt_required()
def get_chapters1(subject_id):
    print(" Received subject_id:", subject_id)  

    identity = get_jwt_identity()  
    print(" Token Data (Chapters Route):", identity)

    try:
        username, course = identity.split(':')
    except ValueError:
        return jsonify({"error": "Invalid token format"}), 400

    conn = get_db()
    chapters = conn.execute('SELECT id, name FROM chapter WHERE subject_id = ?', (subject_id,)).fetchall()
    conn.close()

    return jsonify([{"id": chapter[0], "name": chapter[1]} for chapter in chapters])

##############################-----------------------------------####################3


@app.route('/SignUp', methods=['POST'])
def Register():
    data = request.json

    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    dob = data.get('dob')  
    gender = data.get('gender')
    course = data.get('course')
    name= data.get('name')

   
    if not all([username, password, email, dob, gender, course,name]):
        return jsonify({'success': False, 'error': 'All fields are required.'}),    

    try:
        dob = datetime.datetime.strptime(dob, "%Y-%m-%d").date()
    except ValueError:
        return jsonify({'success': False, 'error': 'Invalid date format.'}), 400



   
    if User.query.filter_by(username=username).first():
        return jsonify({'success': False, 'error': 'Username already exists.'}), 400
    if User.query.filter_by(email=email).first():
        return jsonify({'success': False, 'error': 'Email already exists.'}), 400
    
    hashed_password = generate_password_hash(password)

    
    new_user = User(
        username=username,
        password=hashed_password,
        email=email,
        dob=dob,
        gender=gender,
        course=course,
        name=name,
    )

    
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'success': True, 'message': 'User registered successfully.'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500
    




# -------------------- COURSE FUNCTIONALITY -------------------- #

@app.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return jsonify([{'id': course.id, 'name': course.name} for course in courses])

@app.route('/add-course', methods=['POST'])
@jwt_required()

def add_course():
    data = request.json
    new_course = Course(name=data.get('name'))

    db.session.add(new_course)
    db.session.commit()

    return jsonify({'success': True, 'message': 'Course added successfully'})

@app.route('/delete-course/<int:course_id>', methods=['DELETE'])
@jwt_required()

def delete_course(course_id):
    course = Course.query.get(course_id)
    if course:
        db.session.delete(course)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Course deleted successfully'})
    return jsonify({'error': 'Course not found'}), 404

# -------------------- SUBJECT FUNCTIONALITY -------------------- #

@app.route('/subjects/<int:course_id>', methods=['GET'])
def get_subjects(course_id):
    subjects = Subject.query.filter_by(course_id=course_id).all()
    return jsonify([
        {'id': subject.id, 'name': subject.name, 'courseId': subject.course_id}
        for subject in subjects
    ])


@app.route('/add-subject', methods=['POST'])
@jwt_required()
def add_subject():
    data = request.json
    new_subject = Subject(name=data.get('name'), course_id=data.get('course_id'))

    db.session.add(new_subject)
    db.session.commit()

    return jsonify({'success': True, 'message': 'Subject added successfully'}),201


@app.route('/delete-subject/<int:subject_id>', methods=['DELETE'])
@jwt_required()

def delete_subject(subject_id):
    subject = Subject.query.get(subject_id)
    if subject:
        db.session.delete(subject)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Subject deleted successfully'})
    return jsonify({'error': 'Subject not found'}), 404

# -------------------- CHAPTER FUNCTIONALITY -------------------- #

@app.route('/chapters/<int:subject_id>/<int:course_id>', methods=['GET'])

def get_chapters(subject_id, course_id):
    subject = Subject.query.filter_by(id=subject_id, course_id=course_id).first()
    if not subject:
        return jsonify({'error': 'Subject not found for this course'}), 404

    chapters = Chapter.query.filter_by(subject_id=subject.id).all()
    return jsonify([
        {'id': chapter.id, 'name': chapter.name, 'subjectId': chapter.subject_id, 'courseId': subject.course_id}
        for chapter in chapters
    ])

@app.route('/add-chapter', methods=['POST'])
@jwt_required()
def add_chapter():
    data = request.json
    new_chapter = Chapter(name=data.get('name'), subject_id=data.get('subject_id'))

    db.session.add(new_chapter)
    db.session.commit()

    return jsonify({'success': True, 'message': 'Chapter added successfully'})

@app.route('/delete-chapter/<int:chapter_id>', methods=['DELETE'])
@jwt_required()
def delete_chapter(chapter_id):
    chapter = Chapter.query.get(chapter_id)
    if chapter:
        db.session.delete(chapter)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Chapter deleted successfully'})
    return jsonify({'error': 'Chapter not found'}), 404


@app.route('/edit-course/<int:course_id>', methods=['PUT'])
@jwt_required()
def edit_course(course_id):
    data = request.json
    conn = get_db()
    conn.execute('UPDATE course SET name = ? WHERE id = ?', (data.get('name'), course_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Course updated successfully'})

# Edit Subject Route
@app.route('/edit-subject/<int:subject_id>', methods=['PUT'])
@jwt_required()
def edit_subject(subject_id):
    data = request.json
    conn = get_db()
    conn.execute('UPDATE subject SET name = ? WHERE id = ?', (data.get('name'), subject_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Subject updated successfully'})

# Edit Chapter Route
@app.route('/edit-chapter/<int:chapter_id>', methods=['PUT'])
@jwt_required()
def edit_chapter(chapter_id):
    data = request.json
    conn = get_db()
    conn.execute('UPDATE chapter SET name = ? WHERE id = ?', (data.get('name'), chapter_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Chapter updated successfully'})



#####--------Quiz_Management --------------------#################

@app.route('/api/get_questions/<int:chapter_id>', methods=['GET'])
@jwt_required()
def get_questions(chapter_id):
    print(f"Received request for chapter_id: {chapter_id}")
    try:
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = """
        SELECT 
            q.id, 
            q.text, 
            o.text AS option_text, 
            o.is_correct 
        FROM 
            question q 
        JOIN 
            option o ON q.id = o.question_id 
        WHERE 
            q.chapter_id = ?
        """

        cursor.execute(query, (chapter_id,))
        data = cursor.fetchall()

        questions = {}
        for row in data:
            question_id, question_text, option_text, is_correct = row
            if question_id not in questions:
                questions[question_id] = {
                    'id': question_id,
                    'text': question_text,
                    'options': [],
                    'correctAnswer': None
                }
            questions[question_id]['options'].append({'text': option_text})
            if is_correct == 1:
                questions[question_id]['correctAnswer'] = option_text

        connection.close()
        return jsonify(list(questions.values()))

    except Exception as e:
        return jsonify({'error': 'Failed to fetch questions', 'details': str(e)}), 500


@app.route('/api/edit_question/<int:question_id>', methods=['PUT'])
@jwt_required()
def edit_question(question_id):

    data = request.json

    question = Question.query.get(question_id)
    if not question:
        return jsonify({"error": "Question not found"}), 404

    question.text = data['question']
    Option.query.filter_by(question_id=question.id).delete() 
    for option_text in data['options']:
        is_correct = (option_text == data['correctAnswer'])
        new_option = Option(text=option_text, is_correct=is_correct, question_id=question.id)
        db.session.add(new_option)

    db.session.commit()
    return jsonify({"message": "Question updated successfully!"})


@app.route('/api/delete_question/<int:question_id>', methods=['DELETE'])
@jwt_required()
def delete_question(question_id):
    question = Question.query.get(question_id)
    if not question:
        return jsonify({"error": "Question not found"}), 404

    Option.query.filter_by(question_id=question.id).delete()
    db.session.delete(question)
    db.session.commit()
    return jsonify({"message": "Question deleted successfully!"})


@app.route('/api/questions', methods=['POST'])
@jwt_required()
def add_question():
    data = request.json

    # Step 1: Add the Question
    new_question = Question(
        text=data.get('question'),
        chapter_id=data.get('chapter')
    )
    db.session.add(new_question)
    db.session.commit()

    # Step 2: Add Options
    options_data = data.get('options', [])
    correct_answer = data.get('correctAnswer')

    for option_text in options_data:
        is_correct = option_text == correct_answer
        new_option = Option(
            text=option_text,
            is_correct=is_correct,
            question_id=new_question.id  # Link options to the newly created question
        )
        db.session.add(new_option)

    db.session.commit()

    return jsonify({
        'success': True,
        'message': 'Question and options added successfully!',
        'question_id': new_question.id
    })


########----------------------------End-----------------------------------#######



@app.route('/submit-quiz', methods=['POST'])
@jwt_required()
def submit_quiz():
    identity = get_jwt_identity() 
    print(" Protected Route - Token Data:", identity)

    try:
        username, course = identity.split(':') 
    except ValueError:
        return jsonify({"error": "Invalid token format"}), 400
    
    data = request.get_json()
    print(" Received data:", data)
    
    # Data validation
    if not data:
        return jsonify({"error": "Invalid or missing JSON data"}), 400
    


    quiz_name = data.get('quizName')
    user_id = username
    user_answers = data.get('userAnswers') or data.get('userAnswersObject') or {}


    if not quiz_name or not user_id:
        return jsonify({"error": "quizName or userID missing"}), 400

    if not isinstance(user_answers, dict):
        return jsonify({"error": "Invalid data format for userAnswers"}), 400

    # Database connection
    try:
        conn = get_db()
    except Exception as e:
        return jsonify({"error": f"Database connection error: {str(e)}"}), 500

    
    correct_answers = conn.execute('''
        SELECT q.id, o.text AS correct_answer
        FROM question q
        JOIN option o ON q.id = o.question_id
        WHERE o.is_correct = 1 AND q.chapter_id = (
            SELECT id FROM chapter WHERE name = ?
        )
    ''', (quiz_name,)).fetchall()

    if not correct_answers:
        return jsonify({"error": "No questions found for this quiz"}), 404

    correct_answer_dict = {str(row[0]): row[1] for row in correct_answers}

    
    score = sum(5 for q_id, selected_option in user_answers.items()
                if correct_answer_dict.get(q_id) == selected_option)

    ist_time = datetime.datetime.now(ZoneInfo("Asia/Kolkata"))
    conn.execute('''
        INSERT INTO quiz_result (user_id, quiz_name, duration, questions_count, score, submission_time)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        user_id,
        quiz_name,
        data.get('duration', 0),
        len(correct_answers),
        score,
        ist_time
    ))

    conn.commit()
    conn.close()

    return jsonify({"message": "Quiz submitted successfully!", "score": score})

@app.route('/get-questions', methods=['GET'])
@jwt_required()
def getquestions():
    quiz_name = request.args.get('quizName')
    duration = request.args.get('duration')
    questions_count = request.args.get('questions')

    print(f"Received quizName={quiz_name}, duration={duration}, questions={questions_count}")

    if not quiz_name or not duration or not questions_count:
        return jsonify({"error": "Missing quiz parameters"}), 400

    questions_count = int(questions_count)

    conn = get_db()
    questions = conn.execute('''
        SELECT q.id, q.text, o.id AS option_id, o.text AS option_text
        FROM question q
        JOIN option o ON q.id = o.question_id
        WHERE q.id IN (
            SELECT id 
            FROM question 
            WHERE chapter_id = (
                SELECT id 
                FROM chapter 
                WHERE name = ?
            )
            LIMIT ?
        )
    ''', (quiz_name, questions_count)).fetchall()

    conn.close()

    if not questions:
        print(" No questions fetched. Check chapter name or DB data.")

    result = {}
    for row in questions:
        q_id = row[0]
        if q_id not in result:
            result[q_id] = {
                'id': q_id,
                'text': row[1],
                'options': []
            }
        result[q_id]['options'].append({
            'id': row[2],
            'text': row[3]
        })

    return jsonify(list(result.values()))


@app.route('/leaderboard', methods=['GET'])
@jwt_required()
def get_leaderboard():
    identity = get_jwt_identity()
    try:
        username, _ = identity.split(":")
    except ValueError:
        return jsonify({"error": "Invalid token format"}), 400

    # Count total quiz attempts per user
    results = db.session.query(
        QuizResult.user_id,
        db.func.count(QuizResult.id).label('attempts')
    ).group_by(QuizResult.user_id).order_by(db.desc('attempts')).all()

    leaderboard = []
    user_rank = None

    for idx, row in enumerate(results, start=1):
        leaderboard.append({
            "username": row.user_id,
            "score": row.attempts  # score == total attempts
        })

        if row.user_id == username:
            user_rank = idx

    return jsonify({
        "leaderboard": leaderboard,
        "userRank": user_rank,
        "currentUser": username
    })

@app.route('/score-history', methods=['GET'])
@jwt_required()
def get_score_history():
    identity = get_jwt_identity()
    try:
        username, _ = identity.split(":")
    except ValueError:
        return jsonify({"error": "Invalid token format"}), 400

    results = QuizResult.query.filter_by(user_id=username).order_by(QuizResult.submission_time.desc()).all()

    score_data = [{
        "quiz_name": result.quiz_name,
        "score": result.score,
        "timestamp": result.submission_time.strftime("%Y-%m-%d %H:%M:%S")
    } for result in results]

    return jsonify(score_data)

@app.route('/past_attempts', methods=['GET'])
@jwt_required()
def get_past_attempts():
    identity = get_jwt_identity()
    try:
        username, _ = identity.split(":")
    except ValueError:
        return jsonify({"error": "Invalid token format"}), 400

    attempts = QuizResult.query.filter_by(user_id=username).order_by(QuizResult.submission_time.desc()).all()

    results = []
    for row in attempts:
        results.append({
            "quiz_name": row.quiz_name,
            "submission_time": row.submission_time.strftime('%Y-%m-%d %H:%M:%S')
        })

    return jsonify({"attempts": results}), 200
@app.route('/api/quiz-attempts', methods=['GET'])
@jwt_required()
def get_quiz_attempts():
   
    results = db.session.query(
        QuizResult.quiz_name,
        func.count((QuizResult.user_id)).label('attempts')
    ).group_by(QuizResult.quiz_name).all()

    
    response_data = []
    for quiz_name, attempts in results:
        subject = Subject.query.filter_by(name=quiz_name).first()
        subject_name = subject.name if subject else quiz_name  
        response_data.append({
            'subject': subject_name,
            'attempts': attempts
        })

    return jsonify(response_data)


@app.route('/api/user/<string:user_id>', methods=['GET'])
@jwt_required()
def get_user_by_id(user_id):
    user = User.query.filter_by(username=user_id).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({
        'id': user.id,
        'username': user.username,
        'name': user.name,
        'email': user.email,
        'dob': user.dob.strftime('%Y-%m-%d'),
        'gender': user.gender,
        'course': user.course
    })

@app.route('/download-report')
@jwt_required()
def download_report():
    identity = get_jwt_identity()
    print(" Token Identity:", identity)

    try:
        username, course = identity.split(':')
    except ValueError:
        return jsonify({"error": "Invalid token format"}), 400

    conn = get_db()
    cursor = conn.cursor()

    # Fetch quiz report data
    cursor.execute("""
        SELECT quiz_name, score, duration, submission_time
        FROM quiz_result
        WHERE user_id = ?
    """, (username,))  # username is acting as user_id here

    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return jsonify({"error": "No report data found for this user."}), 404

    
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Quiz Name", "Score", "Duration", "Submission Time"]) 

    for row in rows:
        writer.writerow([row[0], row[1], row[2], row[3]])

    output.seek(0)

    return send_file(
        io.BytesIO(output.getvalue().encode('utf-8')),
        mimetype='text/csv',
        as_attachment=True,
        download_name=f'report_{username}.csv'
    )


@app.route('/send-reminder', methods=['POST'])
@jwt_required()
def send_reminder():
    
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name, email FROM user")
    users = cursor.fetchall()
    conn.close()

    
    sender_email = "ujjawalrauniyar2004@gmail.com"
    sender_password = "cifylmcwkflrwwes" 
    subject = "🚨 New Quiz Available - Boost Your Grades!"

    for user in users:
        name = user[0]
        email = user[1]

        
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = email
        message["Subject"] = subject

        html_content = f"""
        <html>
            <body>
                <h2>Hey {name},</h2>
                <p>A new quiz has just been created on Q-Fi! 🎉</p>
                <p>Attempt it now to ace your grades and stay ahead in the course.</p>
                <p><a href="http://localhost:8080/">Click here to take the quiz!</a></p>
                <br>
                <p>Cheers,<br>Q-Fi Team</p>
            </body>
        </html>
        """
        message.attach(MIMEText(html_content, "html"))

        
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, email, message.as_string())
        except Exception as e:
            print(f"❌ Failed to send to {email}: {e}")

    return jsonify({"message": "Reminders sent successfully!"}) 




@app.route('/submit_quiz_rating', methods=['POST'])

def submit_quiz_rating():
    data = request.json
    username = data.get('username')
    quizname = data.get('quizname')
    rating = data.get('rating')
    timestamp = datetime.datetime.now() 

    # Input validation
    if not username or not quizname or not rating:
        return jsonify({'error': 'Missing required fields'}), 400

    if not (1 <= int(rating) <= 5):
        return jsonify({'error': 'Rating must be between 1 and 5'}), 400

    new_rating = QuizRating(
        username=username,
        quiz_name=quizname,
        rating=int(rating),
        timestamp=timestamp
    )

    db.session.add(new_rating)
    db.session.commit()

    return jsonify({'message': 'Rating submitted successfully'}), 201


@app.route('/api/quiz-average-ratings', methods=['GET'])
@jwt_required()
def get_quiz_average_ratings():
    results = (
        db.session.query(QuizRating.quiz_name, func.avg(QuizRating.rating))
        .group_by(QuizRating.quiz_name)
        .all()
    )

    response = [
        {"quiz_name": quiz, "average_rating": round(avg_rating, 2)}
        for quiz, avg_rating in results
    ]
    return jsonify(response)

@app.route('/api/user-reviews', methods=['GET'])
@jwt_required()
def get_user_reviews():
    reviews = Review2.query.order_by(Review2.id.desc()).all()
    response = [
        {"username": r.username, "review": r.review}
        for r in reviews
    ]
    return jsonify(response)




@app.after_request
def disable_caching(response):
    response.headers["Cache-Control"] = "no-store"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response


from io import StringIO
from email.message import EmailMessage



##################-----Sending Monthly Report--------###############
@app.route('/send-monthly-reminder', methods=['POST'])
@jwt_required()
def send_monthly_reports():
    try:
        ist_time = datetime.datetime.now(ZoneInfo("Asia/Kolkata"))
        one_month_ago = ist_time - timedelta(days=30)
        users = User.query.all()

        print(f" Found {len(users)} users in DB")

        for user in users:
            results = (
                QuizResult.query
                .filter(
                    QuizResult.user_id == user.username,
                    QuizResult.submission_time >= one_month_ago
                )
                .all()
            )

            print(f"📩 Checking user: {user.username} | Results: {len(results)}")

            if results:
                csv_data = generate_csv_for_user(user, results)
                send_email(user.email, csv_data)
                print(f"Email sent to {user.email}")
            else:
                print("⏩ No recent results. Skipping...")

        return jsonify({"message": "Monthly reports sent successfully"}), 200

    except Exception as e:
        print(f" Error occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500


def generate_csv_for_user(user, results):
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(['QuizName', 'Duration', 'No. of Questions', 'Score', 'Submission'])

    for result in results:
        writer.writerow([
            result.quiz_name,
            result.duration,
            result.questions_count,
            result.score,
            result.submission_time.strftime("%Y-%m-%d %H:%M:%S")
        ])
    return output.getvalue()


def send_email(email_to, csv_content):
    sender_email = 'ujjawalrauniyar2004@gmail.com'
    sender_password = 'cifylmcwkflrwwes'  # ⚠️ Replace with secure env variable in production

    msg = EmailMessage()
    msg['Subject'] = "Your Monthly Quiz Performance Report"
    msg['From'] = sender_email
    msg['To'] = email_to
    msg.set_content(" Hey there , Hope you had aced your marks last month. Please find attached your quiz performance report.")
    msg.add_attachment(csv_content.encode('utf-8'), maintype='text', subtype='csv', filename='report.csv')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)


###################################################################

if __name__ == '__main__':
    app.run(debug=True)