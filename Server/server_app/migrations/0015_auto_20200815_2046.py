# Generated by Django 3.0.7 on 2020-08-15 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server_app', '0014_auto_20200815_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdiet',
            name='meal',
            field=models.CharField(choices=[(0, 'Café'), (1, 'Almoço'), (2, 'Jantar'), (3, 'Snacks')], default=None, max_length=1),
        ),
    ]
