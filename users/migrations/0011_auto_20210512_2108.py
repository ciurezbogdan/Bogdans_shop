# Generated by Django 3.1.7 on 2021-05-12 18:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20210505_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activation',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 12, 18, 38, 28, 924838, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='activation',
            name='token',
            field=models.CharField(default='53cce15d5cfa42d7ea5b89e9cc85af05064398c07fcfeb3aa06cac09ac07da2c', max_length=64),
        ),
    ]
