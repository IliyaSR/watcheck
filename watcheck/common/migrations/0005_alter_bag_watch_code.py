# Generated by Django 5.0.1 on 2024-03-31 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_bag_watch_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bag',
            name='watch_code',
            field=models.CharField(max_length=20),
        ),
    ]
