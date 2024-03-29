# Generated by Django 5.0.1 on 2024-03-04 20:31

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
                ('main_image', models.ImageField(upload_to='images/')),
                ('image_for_shop_page', models.ImageField(upload_to='images/')),
                ('first_small_image', models.ImageField(upload_to='images/')),
                ('second_small_image', models.ImageField(upload_to='images/')),
                ('third_small_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('fourth_small_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('brand', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=30)),
                ('details_text', models.TextField()),
                ('watch_code', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('case_material', models.CharField(max_length=30)),
                ('strap_material', models.CharField(max_length=30)),
                ('movement', models.CharField(max_length=30)),
                ('water_resistance', models.IntegerField()),
                ('case_diameter', models.IntegerField()),
                ('case_thickness', models.FloatField()),
                ('glass', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Watch',
                'verbose_name_plural': 'Watches',
            },
        ),
    ]
