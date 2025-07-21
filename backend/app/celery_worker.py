from app import create_app
from celery import Celery
from celery.schedules import crontab

# Create the Flask app
flask_app = create_app()

# Initialize Celery with Flask app context
celery = Celery(
    __name__,
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

# Update Celery config from Flask app config
celery.conf.update(flask_app.config)

# Register periodic tasks
celery.conf.beat_schedule = {
    'send-monthly-report': {
        'task': 'app.tasks.send_monthly_reports',
        'schedule': crontab(minute='*/1'),
    }
}

# Make sure app.tasks gets imported so tasks get registered
with flask_app.app_context():
    import app.tasks
