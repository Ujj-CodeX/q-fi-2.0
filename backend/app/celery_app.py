# app/celery_app.py

from celery import Celery

def make_celery(app_name=__name__):
    return Celery(
        app_name,
        broker='redis://localhost:6379/0',
        backend='redis://localhost:6379/0'
    )

celery = make_celery()


from celery.schedules import crontab
celery.conf.beat_schedule = {
    'send-monthly-report': {
        'task': 'app.tasks.send_monthly_reports',
        'schedule': crontab(minute='*/1'),
    }
}
