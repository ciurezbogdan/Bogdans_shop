# Generated by Django 3.1.7 on 2021-05-05 11:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_activation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activation',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 5, 12, 4, 33, 287929, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='activation',
            name='token',
            field=models.CharField(default='b822520260cd227bd2c1a4d237e7ecf4b3781fbbf9f6da6998a7b9d95f807fc6', max_length=64),
        ),
    ]
