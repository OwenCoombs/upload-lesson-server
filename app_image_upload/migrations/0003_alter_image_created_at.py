# Generated by Django 5.0.6 on 2024-06-05 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_image_upload', '0002_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
