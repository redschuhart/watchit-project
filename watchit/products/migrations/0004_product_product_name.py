# Generated by Django 4.2.7 on 2023-11-29 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_productcategory_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_name',
            field=models.CharField(default='Name uknown', max_length=255),
        ),
    ]