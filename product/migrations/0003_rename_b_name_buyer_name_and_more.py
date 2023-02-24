# Generated by Django 4.1.5 on 2023-02-13 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_buyer_company_name_supplier_company_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyer',
            old_name='b_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='p_name',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='s_name',
            new_name='name',
        ),
    ]
