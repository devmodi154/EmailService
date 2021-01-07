from django.core.mail import send_mail
from django.conf import settings
from django.core import mail

class SendGridService():
    def __init__(self)-> None:
        self.connection = mail.get_connection()
        
    def setup(self)-> None:    
        self.connection.password = settings.EMAIL_HOST_PASSWORD
        self.connection.username = settings.EMAIL_HOST_USER
        self.connection.host = settings.EMAIL_HOST
        self.connection.port = settings.EMAIL_PORT
        self.connection.use_tls = settings.EMAIL_USE_TLS
        return self.connection


