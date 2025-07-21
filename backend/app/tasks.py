from app.celery_app import celery
from app.celery_worker import celery
from app.utils import process_and_send_all_quiz_reports,generate_csv_for_user

@celery.task
def send_monthly_reports():
    users = process_and_send_all_quiz_reports()
    for username, email in users:
        csv_data = generate_csv_for_user(username)
        send_email_with_csv(email, username, csv_data)
from app.celery_app import celery
from app.utils import (
    process_and_send_all_quiz_reports,
    generate_csv_for_user,
    send_email_with_csv
)

@celery.task
def send_monthly_reports():
    users = process_and_send_all_quiz_reports()
    
    if not users:
        print("No users to send reports to.")
        return

    for username, email, quiz_data in users:
        try:
            csv_data = generate_csv_for_user(username, quiz_data)
            if csv_data:
                send_email_with_csv(email, username, csv_data)
                print(f"Report sent to {username} at {email}")
            else:
                print(f"CSV data generation failed for {username}")
        except Exception as e:
            print(f"Error sending report to {username} ({email}): {str(e)}")
