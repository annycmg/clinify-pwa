# Generated by Django 3.0.8 on 2020-08-19 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server_app', '0020_userprofile_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='slug',
        ),
    ]
