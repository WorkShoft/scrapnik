# Generated by Django 3.0.3 on 2020-02-22 20:57

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('tables', '0007_auto_20200222_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 2, 22, 20, 57, 15, 172172, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='table',
            name='name',
            field=models.CharField(max_length=400),
        ),
    ]
