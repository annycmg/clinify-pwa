# Generated by Django 3.0.8 on 2020-08-11 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server_app', '0008_usertrip_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='uservaccine',
            name='slug',
            field=models.SlugField(default='slug'),
        ),
    ]