# Generated by Django 3.2.9 on 2021-11-29 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0012_remove_image_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ManyToManyField(to='images.Location'),
        ),
    ]