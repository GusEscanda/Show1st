# Generated by Django 3.1.1 on 2020-11-09 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ShowBlog', '0007_blogpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='pageFilter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ShowBlog.posttag', verbose_name='Filter Tag'),
        ),
    ]
