# Generated by Django 4.1.7 on 2023-03-30 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Foodie_Zone', '0025_alter_items_image_cart'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
