# Generated by Django 3.1.1 on 2020-10-31 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShowBlog', '0005_auto_20201025_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postContent',
            field=models.TextField(verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='postTitle',
            field=models.CharField(max_length=60, verbose_name='Title'),
        ),
    ]