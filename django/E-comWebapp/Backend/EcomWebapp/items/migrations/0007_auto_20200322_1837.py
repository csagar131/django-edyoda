# Generated by Django 2.2.10 on 2020-03-22 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_auto_20200321_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='cat_image',
            field=models.ImageField(upload_to='categories/images'),
        ),
        migrations.AlterField(
            model_name='products',
            name='p_image',
            field=models.ImageField(upload_to='products/images'),
        ),
    ]