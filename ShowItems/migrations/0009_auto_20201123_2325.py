# Generated by Django 3.1.1 on 2020-11-24 02:25

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('ShowItems', '0008_shoppingcart'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemspage',
            name='enableShopCart',
            field=models.BooleanField(default=False, verbose_name='Enable Shopping Cart'),
        ),
        migrations.AddField(
            model_name='itemspage',
            name='footText',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Posterior text'),
        ),
        migrations.AddField(
            model_name='itemspage',
            name='headerText',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Previous text'),
        ),
    ]