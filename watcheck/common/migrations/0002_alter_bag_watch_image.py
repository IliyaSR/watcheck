# Generated by Django 5.0.1 on 2024-03-26 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bag',
            name='watch_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
