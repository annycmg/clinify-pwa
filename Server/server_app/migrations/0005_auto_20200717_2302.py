# Generated by Django 3.0.8 on 2020-07-18 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server_app', '0004_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_age_prf',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_height_prf',
            field=models.IntegerField(),
        ),
    ]