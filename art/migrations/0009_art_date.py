# Generated by Django 4.2.16 on 2025-01-28 10:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0008_art_orientation_art_size_delete_specification'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
