# Generated by Django 5.0.1 on 2024-04-16 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0014_alter_order_current_profile'),
        ('watch', '0006_alter_watch_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='current_watch',
        ),
        migrations.AddField(
            model_name='order',
            name='current_watch',
            field=models.ManyToManyField(to='watch.watch'),
        ),
    ]
