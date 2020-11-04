# Generated by Django 3.1.1 on 2020-11-02 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0009_auto_20201031_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuoption',
            name='optEnabled',
        ),
        migrations.AddField(
            model_name='menuoption',
            name='optNavBar',
            field=models.BooleanField(default=True, verbose_name='Navigation Bar'),
        ),
    ]