# Generated by Django 3.1.7 on 2021-06-15 17:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20210514_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activation',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 15, 18, 29, 52, 315933, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='activation',
            name='token',
            field=models.CharField(default='525fa6b90ef95a120e74e29994d626cfca7055a292265190cd8da5a1f7e95b7a', max_length=64),
        ),
    ]
