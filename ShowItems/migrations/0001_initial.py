# Generated by Django 3.1.1 on 2020-10-25 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catName', models.CharField(max_length=30, unique=True, verbose_name='Category')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Item Category',
                'verbose_name_plural': 'Item Categories',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemCode', models.CharField(db_index=True, max_length=20, verbose_name='Code')),
                ('itemName', models.CharField(max_length=50, verbose_name='Name')),
                ('itemDescrip', models.CharField(max_length=500, verbose_name='Description')),
                ('itemThumb', models.ImageField(upload_to='ShowItems', verbose_name='Small (small)')),
                ('itemImage', models.ImageField(upload_to='ShowItems', verbose_name='Image (big)')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('itemCats', models.ManyToManyField(to='ShowItems.ItemCategory', verbose_name='Categories')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
            },
        ),
    ]
