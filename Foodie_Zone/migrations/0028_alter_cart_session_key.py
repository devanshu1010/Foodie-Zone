# Generated by Django 4.1.7 on 2023-03-31 15:16

import Foodie_Zone.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Foodie_Zone', '0027_cart_cartitem_cartitem_item_cartitem_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='session_key',
            field=models.CharField(blank=True, default=Foodie_Zone.models.generate_unique_key, max_length=32, null=True, unique=True),
        ),
    ]