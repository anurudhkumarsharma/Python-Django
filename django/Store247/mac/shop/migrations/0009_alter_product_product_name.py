# Generated by Django 3.2.9 on 2022-12-30 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_product_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=100),
        ),
    ]
