# Generated by Django 3.0.3 on 2020-02-24 09:26

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAgent',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('percent', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('useragent', models.CharField(max_length=256)),
                ('system', models.CharField(max_length=128)),
            ],
        ),
    ]
