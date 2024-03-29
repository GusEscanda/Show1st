# Generated by Django 3.1.1 on 2020-12-17 19:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ShowBlog', '0013_auto_20201210_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='pageTagFilter',
            field=models.ForeignKey(blank=True, help_text='Display only the posts with this tag, if not specified display all posts', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='ShowBlog.posttag', verbose_name='Filter Tag'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(help_text='Author of the post', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(help_text='Enter the content of the post', verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(db_index=True, default=datetime.date.today, help_text='The date of the post', verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, help_text='Upload a thumbnail image to display with this post', null=True, upload_to='ShowBlog', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(help_text='Select all the tags this post is related to', related_name='posts', to='ShowBlog.PostTag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(help_text='Title of the post', max_length=60, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='posttag',
            name='name',
            field=models.CharField(help_text='Create tags to categorize your posts', max_length=30, unique=True, verbose_name='Tag'),
        ),
    ]
