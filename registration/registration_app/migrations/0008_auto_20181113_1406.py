# Generated by Django 2.1.2 on 2018-11-13 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration_app', '0007_auto_20181113_1403'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='date',
            new_name='registration_date_time',
        ),
    ]
