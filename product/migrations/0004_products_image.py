# Generated by Django 4.1.5 on 2023-02-22 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_b_name_buyer_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]