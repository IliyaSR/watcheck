# Generated by Django 5.0.1 on 2024-03-19 09:09

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_address_current_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='country',
            field=django_countries.fields.CountryField(max_length=40),
        ),
    ]
