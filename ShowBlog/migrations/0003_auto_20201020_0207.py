# Generated by Django 3.1.1 on 2020-10-20 05:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ShowBlog', '0002_post_postdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postDate',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date'),
            preserve_default=False,
        ),
    ]
