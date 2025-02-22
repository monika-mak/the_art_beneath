# Generated by Django 4.2.16 on 2025-02-22 00:41

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0012_alter_art_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='art',
            name='image_2',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='art',
            name='orientation',
            field=models.CharField(choices=[('Horizontal', 'Horizontal'), ('Vertical', 'Vertical'), ('Square', 'Square')], default='Square', max_length=25),
        ),
    ]
