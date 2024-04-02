# Generated by Django 5.0.1 on 2024-03-28 21:28

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_alter_bag_watch_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('town', models.CharField(max_length=20)),
                ('postcode', models.IntegerField()),
                ('phone', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)])),
                ('email', models.EmailField(max_length=202)),
                ('brand_watch', models.CharField(max_length=30)),
                ('current_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]