# Generated by Django 4.1.5 on 2023-02-24 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(null=True, upload_to='image/'),
        ),
    ]
