# Generated by Django 4.1.5 on 2023-02-28 18:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_remove_purchase_status_purchase_avg_buy_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='dop',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
