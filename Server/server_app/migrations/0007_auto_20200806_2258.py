# Generated by Django 3.0.8 on 2020-08-07 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server_app', '0006_usermedication_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermedication',
            name='slug',
            field=models.SlugField(default='slug'),
        ),
    ]