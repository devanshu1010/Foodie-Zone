# Generated by Django 4.1.7 on 2023-04-09 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Foodie_Zone', '0039_cart_cartitem_payment_order_cartitem_item_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
