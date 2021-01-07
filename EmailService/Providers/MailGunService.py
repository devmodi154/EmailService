from django.core.mail import send_mail
from django.conf import settings
from django.core import mail

class MailGunService():
    def __init__(self)-> None:
        self.connection = mail.get_connection()
        
    def setup(self)-> None:    
        self.connection.password = settings.ALTERNATE_EMAIL_HOST_PASSWORD
        self.connection.username = settings.ALTERNATE_EMAIL_HOST_USER
        self.connection.host = settings.ALTERNATE_EMAIL_HOST
        self.connection.port = settings.ALTERNATE_EMAIL_PORT
        self.connection.use_tls = settings.ALTERNATE_EMAIL_USE_TLS
        return self.connection