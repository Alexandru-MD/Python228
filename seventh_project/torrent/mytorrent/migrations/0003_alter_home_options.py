# Generated by Django 4.2.5 on 2023-11-08 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mytorrent', '0002_category_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='home',
            options={'ordering': ['-time_created'], 'verbose_name': 'Торрент', 'verbose_name_plural': 'Торренты'},
        ),
    ]
