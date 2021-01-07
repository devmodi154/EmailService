from django.db import models

# Create your models here.
class MailRequests(models.Model):
    email_address = models.EmailField()
    mail_subject = models.CharField(max_length=128)
    mail_body = models.TextField(max_length=1024)