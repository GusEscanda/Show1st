# Generated by Django 3.1.1 on 2020-10-29 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_auto_20201029_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='style',
            name='styleTextBGColor',
            field=models.CharField(blank=True, max_length=100, verbose_name='Text BG color'),
        ),
        migrations.AlterField(
            model_name='style',
            name='styleInfoBoxColor',
            field=models.CharField(blank=True, max_length=100, verbose_name='Info box color'),
        ),
    ]
