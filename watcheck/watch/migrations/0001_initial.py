# Generated by Django 5.0.1 on 2024-02-23 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_image', models.ImageField(upload_to='')),
                ('image_for_shop_page', models.ImageField(upload_to='')),
                ('second_image', models.ImageField(upload_to='')),
                ('third_image', models.ImageField(upload_to='')),
                ('fourth_image', models.ImageField(upload_to='')),
                ('brand', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=30)),
                ('details_text', models.TextField()),
                ('watch_code', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('case_material', models.CharField(max_length=30)),
                ('strap_material', models.CharField(max_length=30)),
                ('movement', models.CharField(max_length=30)),
                ('water_resistance', models.IntegerField()),
                ('case_diameter', models.FloatField()),
                ('case_thickness', models.FloatField()),
                ('glass', models.CharField(max_length=30)),
            ],
        ),
    ]
