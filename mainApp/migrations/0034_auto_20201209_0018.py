# Generated by Django 3.1.1 on 2020-12-09 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0033_auto_20201128_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='style',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pages', to='mainApp.style', verbose_name='Style'),
        ),
    ]
