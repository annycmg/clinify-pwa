# Generated by Django 3.0.8 on 2020-08-21 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server_app', '0023_userappoint'),
    ]

    operations = [
        migrations.AddField(
            model_name='userappoint',
            name='appoint_credenc_apt',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
