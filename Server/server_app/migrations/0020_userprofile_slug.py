# Generated by Django 3.0.8 on 2020-08-18 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server_app', '0019_auto_20200815_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(default='slug'),
        ),
    ]
