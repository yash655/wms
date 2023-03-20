# Generated by Django 4.1.5 on 2023-02-28 19:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_remove_purchase_avg_buy_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='dos',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='sales',
            name='qty',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sales',
            name='total',
            field=models.FloatField(default=0),
        ),
    ]
