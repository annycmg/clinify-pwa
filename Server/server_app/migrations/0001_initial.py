# Generated by Django 3.0.8 on 2020-08-02 23:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserVaccine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine_name_vac', models.CharField(max_length=200)),
                ('vaccine_date_vac', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserTrip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_country_trp', models.CharField(max_length=300)),
                ('init_date_trp', models.DateField()),
                ('end_date_trp', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_age_prf', models.IntegerField()),
                ('profile_loc_prf', models.CharField(max_length=150)),
                ('profile_weight_prf', models.FloatField()),
                ('profile_height_prf', models.IntegerField()),
                ('profile_allergy_prf', models.CharField(max_length=200)),
                ('profile_desease_prf', models.CharField(max_length=200)),
                ('profile_diet_prf', models.CharField(max_length=200)),
                ('profile_surgery_prf', models.CharField(max_length=200)),
                ('profile_exerc_prf', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserMedication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medication_name_med', models.CharField(max_length=200)),
                ('dosis_name_med', models.CharField(max_length=30)),
                ('init_date_med', models.DateField()),
                ('end_date_med', models.DateField()),
                ('time_med', models.TimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserDiet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diet_include', models.TextField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
