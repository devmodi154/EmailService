# Generated by Django 2.1.2 on 2021-01-05 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailRequests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.EmailField(max_length=254)),
                ('mail_subject', models.CharField(max_length=128)),
                ('mail_body', models.TextField(max_length=1024)),
            ],
        ),
    ]
