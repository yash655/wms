# Generated by Django 4.1.5 on 2023-02-13 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='company_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='company_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]