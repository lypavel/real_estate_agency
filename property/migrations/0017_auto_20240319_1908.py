# Generated by Django 2.2.24 on 2024-03-19 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_auto_20240319_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]