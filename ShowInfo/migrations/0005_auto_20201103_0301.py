# Generated by Django 3.1.1 on 2020-11-03 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0010_auto_20201102_1118'),
        ('ShowInfo', '0004_infopage_inflinks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infopage',
            name='infLinks',
            field=models.ManyToManyField(null=True, to='mainApp.MenuOption', verbose_name='Additional Info Links'),
        ),
    ]