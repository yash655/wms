# Generated by Django 4.1.5 on 2023-02-28 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_alter_buyer_gst_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='company_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
