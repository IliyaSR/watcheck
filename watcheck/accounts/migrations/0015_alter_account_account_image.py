# Generated by Django 5.0.1 on 2024-04-09 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_account_account_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]