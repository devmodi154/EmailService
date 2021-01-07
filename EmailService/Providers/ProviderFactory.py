from django.db import connection
from API.settings import EMAIL_HOST
from EmailService.Providers.SendGridService import SendGridService
from EmailService.Providers.MailGunService import MailGunService
from django.conf import settings


class ProviderFactory():
    # Set provider and returns connection
    def setConfigurations(self, provider = None)-> str:
        connection = self.getProvider(provider)
        return connection

    # Alter providers
    def getProvider(self,provider=None)-> dict:
        if provider == 'mailgun':
            return MailGunService().setup()
        else:
            return SendGridService().setup()
