# app/__init__.py

from flask import Flask
from flask_mail import Mail

mail = Mail()

def create_app():
    app = Flask(__name__)
    
    app.config.update(
        MAIL_SERVER='smtp.example.com',
        MAIL_PORT=587,
        MAIL_USERNAME='ujjawalrauniyar2004@gmail.com',
        MAIL_PASSWORD='cifylmcwkflrwwes',
        MAIL_USE_TLS=True,
        MAIL_USE_SSL=False
    )

    mail.init_app(app)

    return app
