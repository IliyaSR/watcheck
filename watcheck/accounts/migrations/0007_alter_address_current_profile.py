# Generated by Django 5.0.1 on 2024-03-25 16:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_address_country_alter_address_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='current_profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
