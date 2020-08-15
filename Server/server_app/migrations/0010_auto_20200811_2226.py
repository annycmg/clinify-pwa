# Generated by Django 3.0.7 on 2020-08-12 01:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('server_app', '0009_uservaccine_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdiet',
            name='diet_date_diet',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdiet',
            name='slug',
            field=models.SlugField(default='slug'),
        ),
    ]