# Generated by Django 3.1.1 on 2020-11-28 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShowContact', '0011_delete_emailhostconfig'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='showSocialMedia',
            field=models.BooleanField(default=False, verbose_name='Show Social Media'),
        ),
    ]