# Generated by Django 5.0 on 2023-12-08 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_flower_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='flower',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='images'),
        ),
    ]
