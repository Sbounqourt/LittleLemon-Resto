# Generated by Django 5.1.1 on 2024-11-06 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_menu_menu_item_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='menu_item_description',
        ),
    ]
