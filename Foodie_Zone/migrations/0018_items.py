# Generated by Django 4.1.7 on 2023-03-12 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Foodie_Zone', '0017_delete_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('image', models.ImageField(upload_to='item')),
                ('ingredients', models.TextField()),
                ('price', models.FloatField()),
                ('is_available', models.BooleanField(default=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('Rest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Foodie_Zone.restaurant')),
            ],
            options={
                'verbose_name_plural': 'Item Table',
            },
        ),
    ]
