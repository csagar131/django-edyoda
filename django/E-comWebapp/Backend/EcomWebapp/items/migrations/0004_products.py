# Generated by Django 2.2.10 on 2020-03-21 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20200321_1945'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_image', models.ImageField(upload_to='items/static/products/images')),
                ('p_name', models.CharField(max_length=50)),
                ('p_price', models.DecimalField(decimal_places=5, max_digits=8)),
                ('p_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='items.Categories')),
            ],
        ),
    ]