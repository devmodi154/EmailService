from EmailService.Providers.SendGridService import SendGridService
from API.settings import EMAIL_ADDRESS, EMAIL_HOST_USER
from EmailService.Providers.ProviderFactory import ProviderFactory
from django.core.mail import send_mail
from django.test import TestCase
from django.test import Client

# Create your tests here.
class ProviderFailSafe(TestCase):
    def setUp(self):
        self.c = Client()
        self.email_address = 'devmodi124@gmail.com'    

    def test_SendGrid_Service(self):
        response = self.c.post(
            '/API/',
            {
                'email_address': self.email_address,
                 'mail_subject': 'SendGrid TEST',
                 'mail_body': 'WORKING!',
        })
        assert response.status_code == 201

    def test_MailGun_Service(self):
        # Faulting email to let the Fail Safe action take place
        response = self.c.post(
            '/API/',
            {
                'email_address': self.email_address,
                 'mail_subject': 'MailGun TEST',
                 'mail_body': 'WORKING!',
        })
        assert response.status_code == 201

class EmailServiceWorking(TestCase):
    def setUp(self):
        self.connection = ProviderFactory().setConfigurations()
        self.email_address = 'devmodi124@gmail.com'
        
    def test_SendGrid_Service(self):
        assert True == send_mail(
            "SendGrid TEST",
            "WORKING!",
            EMAIL_ADDRESS,
            [self.email_address],
            connection=self.connection,
            fail_silently=False )

    def test_MailGun_Service(self):
        self.connection = ProviderFactory().setConfigurations('mailgun')
        assert True == send_mail(
            "MailGun TEST",
            "WORKING!",
            EMAIL_ADDRESS,
            [self.email_address],
            connection=self.connection,
            fail_silently=False )