# Generated by Django 3.2.9 on 2021-11-29 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0010_alter_image_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='location',
            field=models.ForeignKey(default='', null=None, on_delete=django.db.models.deletion.CASCADE, to='images.location'),
        ),
    ]
