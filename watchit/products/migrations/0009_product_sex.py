# Generated by Django 4.2.7 on 2023-11-29 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_productbrand_brand_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sex',
            field=models.CharField(default='Мужские', max_length=255),
        ),
    ]