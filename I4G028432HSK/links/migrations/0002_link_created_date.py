# Generated by Django 4.0.6 on 2022-07-10 19:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 10, 20, 23, 13, 960132)),
        ),
    ]
