# Generated by Django 3.1.7 on 2021-06-15 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20210512_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='products/'),
        ),
    ]