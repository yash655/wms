# Generated by Django 4.1.5 on 2023-02-28 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_rename_avg_price_products_avg_buy_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='avg_buy_price',
        ),
    ]