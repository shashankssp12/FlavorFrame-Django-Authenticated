# Generated by Django 5.1.7 on 2025-03-10 11:35

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FlavorFrame', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='Rimage',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
