# Generated by Django 3.0.8 on 2020-07-17 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserVaccine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine_name_vac', models.CharField(max_length=200)),
                ('vaccine_date_vac', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='usermedication',
            name='time_med',
            field=models.TimeField(),
        ),
    ]
