# Generated by Django 4.2.5 on 2023-09-15 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_brand_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Availability',
            field=models.CharField(choices=[('In Stock', 'In Stock'), ('Out of Stock', 'Out of Stock')], max_length=100, null=True),
        ),
    ]
