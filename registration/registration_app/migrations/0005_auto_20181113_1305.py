# Generated by Django 2.1.2 on 2018-11-13 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_app', '0004_user_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]