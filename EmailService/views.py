# from django.shortcuts import render
from API.settings import EMAIL_ADDRESS
from django.db import connection
from EmailService.Providers.ProviderFactory import ProviderFactory
from django.core.mail import send_mail
from EmailService.models import MailRequests
from rest_framework import status
from rest_framework.response import Response
from .serializers import MailSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def response_mail(request)-> Response:
    if request.method == 'GET':
        mailing_list = MailRequests.objects.all()
        serializer = MailSerializer(mailing_list, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Retrieving Form Data 
        to_email_address = request.POST['email_address']
        mail_subject = request.POST['mail_subject']
        mail_body = request.POST['mail_body']

        # Setting SMTP connection
        connection = ProviderFactory().setConfigurations('mailgun')

        serializer = MailSerializer(data=request.data)
        # Small template for mail
        html_message = '<blockquote>'+mail_body+'</blockquote><br>'+'<strong>Thank you for using our service!</strong>'

        # Fail safe mech using multiple providers to send mail
        try:
            send_mail(
                mail_subject,
                mail_body,
                EMAIL_ADDRESS,
                [to_email_address],
                connection=connection,
                html_message= html_message,
                fail_silently=False)
        except Exception as e:
            try:
                connection = ProviderFactory().setConfigurations('mailgun')
                send_mail(
                    mail_subject,
                    mail_body,
                    EMAIL_ADDRESS,
                    [to_email_address],
                    connection=connection,
                    html_message= html_message,
                    fail_silently=False) 
            except Exception as e:
                # print("No provider available!")
                # print(e) LOGGING
                return Response(serializer.data, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
