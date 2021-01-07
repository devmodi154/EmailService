from EmailService.models import MailRequests
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MailRequests
        fields = ('id','email_address','mail_subject','mail_body',)
