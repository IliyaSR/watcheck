# Generated by Django 5.0.1 on 2024-04-15 13:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_alter_account_email_alter_account_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]
