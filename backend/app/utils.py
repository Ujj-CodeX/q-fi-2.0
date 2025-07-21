import csv
import smtplib
from email.message import EmailMessage
from datetime import datetime, timedelta
from io import StringIO
from model import db
from model import User, QuizResult, Course, Subject, Chapter, Question

# CSV EXPORT FUNCTION
def generate_csv_for_user(user, results):
    
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(['Course', 'Subject', 'Chapter', 'Question', 'Correct', 'Timestamp'])

    for result in results:
        question = Question.query.get(result.question_id)
        chapter = Chapter.query.get(question.chapter_id)
        subject = Subject.query.get(chapter.subject_id)
        course = Course.query.get(subject.course_id)

        writer.writerow([
            course.course_name,
            subject.subject_name,
            chapter.chapter_name,
            question.question_text,
            "Yes" if result.is_correct else "No",
            result.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        ])

    return output.getvalue()


# EMAIL FUNCTION
def send_email_with_csv(recipient_email, username, csv_content):
    """
    Sends an email to the user with the CSV report as attachment
    """
    sender_email = "ujjawalrauniyar2004@gmail.com"  # Replace with yours
    sender_password = "cifylmcwkflrwwes"   # App password (Gmail App Password)

    msg = EmailMessage()
    msg['Subject'] = f"Your Monthly Quiz Report - {datetime.now().strftime('%B %Y')}"
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg.set_content(f"Hi {username},\n\nPlease find your monthly quiz report attached.\n\nBest,\nQ-Fi Team")

    msg.add_attachment(
        csv_content,
        subtype='csv',
        filename=f'{username}_quiz_report.csv'
    )

    # Send the email using Gmail SMTP
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)


# MAIN SUMMARY + MAIL DISPATCH FUNCTION
def process_and_send_all_quiz_reports():
    """
    Main utility to be called from Celery: generate reports and send email to all users.
    """
    one_month_ago = datetime.now() - timedelta(days=30)
    users = User.query.all()

    for user in users:
        results = (
            QuizResult.query
            .filter_by(user_id=user.id)
            .filter(QuizResult.timestamp >= one_month_ago)
            .all()
        )

        if not results:
            continue  # Skip users with no activity

        csv_content = generate_csv_for_user(user, results)
        send_email_with_csv(user.email, user.username, csv_content)
