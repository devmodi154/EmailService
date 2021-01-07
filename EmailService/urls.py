from EmailService.views import response_mail
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include

urlpatterns = [
    path('', response_mail),
]