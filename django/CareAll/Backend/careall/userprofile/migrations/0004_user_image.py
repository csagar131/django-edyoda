# Generated by Django 2.2.10 on 2020-05-16 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20200516_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile/'),
        ),
    ]
