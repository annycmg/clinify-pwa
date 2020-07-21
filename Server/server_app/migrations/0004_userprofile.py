# Generated by Django 3.0.8 on 2020-07-18 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server_app', '0003_usertrip'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_age_prf', models.IntegerField(max_length=3)),
                ('profile_loc_prf', models.CharField(max_length=150)),
                ('profile_weight_prf', models.FloatField()),
                ('profile_height_prf', models.IntegerField(max_length=3)),
                ('profile_allergy_prf', models.CharField(max_length=200)),
                ('profile_desease_prf', models.CharField(max_length=200)),
                ('profile_diet_prf', models.CharField(max_length=200)),
                ('profile_surgery_prf', models.CharField(max_length=200)),
                ('profile_exerc_prf', models.CharField(max_length=200)),
            ],
        ),
    ]