# Generated by Django 2.2.24 on 2024-03-19 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_complaint'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='complaint',
            options={'verbose_name': 'Жалоба', 'verbose_name_plural': 'Жалобы'},
        ),
        migrations.AlterModelOptions(
            name='flat',
            options={'verbose_name': 'Квартира', 'verbose_name_plural': 'Квартиры'},
        ),
    ]
