# Generated by Django 5.2.1 on 2025-05-14 11:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0003_category_category_name_en_category_category_name_ru_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='online_store.product'),
        ),
    ]
