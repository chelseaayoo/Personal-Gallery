# Generated by Django 3.2.9 on 2021-11-29 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0009_auto_20211129_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='location',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='images.location'),
        ),
    ]