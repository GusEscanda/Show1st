# Generated by Django 3.1.1 on 2020-11-28 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0032_auto_20201128_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='emailHost',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Email Host'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='emailHostPassword',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Email Host Password'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='emailHostUser',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Email Host User'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='emailPort',
            field=models.PositiveIntegerField(blank=True, default=587, verbose_name='Email Port'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='emailUseSSL',
            field=models.BooleanField(default=False, verbose_name='Email Use SSL'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='emailUseTLS',
            field=models.BooleanField(default=False, verbose_name='Email Use TLS'),
        ),
    ]