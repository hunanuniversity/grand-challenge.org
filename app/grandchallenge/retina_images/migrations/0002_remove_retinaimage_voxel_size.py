# Generated by Django 2.1.4 on 2018-12-17 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retina_images', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='retinaimage',
            name='voxel_size',
        ),
    ]