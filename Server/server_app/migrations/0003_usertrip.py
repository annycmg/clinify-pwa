# Generated by Django 3.0.8 on 2020-07-17 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server_app', '0002_auto_20200716_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTrip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_country_trp', models.CharField(max_length=300)),
                ('init_date_trp', models.DateField()),
                ('end_date_trp', models.DateField()),
            ],
        ),
    ]