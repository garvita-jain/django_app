# Generated by Django 3.0.8 on 2020-08-01 07:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(default='Other', max_length=6),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_no',
            field=models.CharField(default='0', max_length=10),
        ),
    ]
