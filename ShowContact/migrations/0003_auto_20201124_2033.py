# Generated by Django 3.1.1 on 2020-11-24 23:33

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('ShowContact', '0002_subjectoption'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.SlugField(max_length=10, unique=True, verbose_name='Order')),
                ('name', models.CharField(max_length=20, verbose_name='Contact channel')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='ShowContact', verbose_name='Icon')),
                ('info', models.CharField(max_length=50, verbose_name='Contact info')),
            ],
        ),
        migrations.CreateModel(
            name='MailTo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.EmailField(max_length=100, unique=True, verbose_name='Mail Address')),
            ],
        ),
        migrations.AddField(
            model_name='contactpage',
            name='enableShopCart',
            field=models.BooleanField(default=False, verbose_name='Enable Shopping Cart'),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='text_1',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Text 1'),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='text_2',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Text 2'),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='text_3',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Text 3'),
        ),
        migrations.AlterField(
            model_name='subjectoption',
            name='subject',
            field=models.CharField(max_length=100, unique=True, verbose_name='Subject'),
        ),
    ]
