# Generated by Django 3.0.7 on 2020-08-15 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server_app', '0011_userdiet_meal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdiet',
            name='meal',
            field=models.CharField(choices=[(1, 'Café'), (2, 'Almoço'), (3, 'Jantar'), (4, 'Lanche')], default=None, max_length=1),
        ),
    ]
