# Generated by Django 3.0.8 on 2020-08-07 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server_app', '0005_auto_20200802_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermedication',
            name='slug',
            field=models.SlugField(default='slug', editable=False),
        ),
    ]
