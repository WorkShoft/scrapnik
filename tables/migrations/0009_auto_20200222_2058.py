# Generated by Django 3.0.3 on 2020-02-22 20:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('tables', '0008_auto_20200222_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
