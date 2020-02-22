# Generated by Django 3.0.3 on 2020-02-20 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0002_auto_20200220_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='table',
            name='url',
            field=models.CharField(default='google.com', max_length=2048),
        ),
    ]