# Generated by Django 3.1.1 on 2020-11-03 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0010_auto_20201102_1118'),
        ('ShowInfo', '0005_auto_20201103_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infopage',
            name='infLinks',
            field=models.ManyToManyField(blank=True, to='mainApp.MenuOption', verbose_name='Additional Info Links'),
        ),
    ]