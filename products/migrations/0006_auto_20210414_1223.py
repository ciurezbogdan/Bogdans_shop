# Generated by Django 3.1.7 on 2021-04-14 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0005_auto_20210331_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.ManyToManyField(related_name='products', through='products.ProductCategories', to='products.Category'),
        ),
        migrations.AlterField(
            model_name='products',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL),
        ),
    ]
