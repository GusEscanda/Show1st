# Generated by Django 3.1.1 on 2020-11-26 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShowContact', '0009_auto_20201126_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailhostconfig',
            name='configId',
            field=models.PositiveIntegerField(default=1, unique=True),
        ),
    ]
