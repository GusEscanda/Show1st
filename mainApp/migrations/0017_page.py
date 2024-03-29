# Generated by Django 3.1.1 on 2020-11-09 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0016_delete_option'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(choices=[('HOM', 'Home'), ('INF', 'ShowInfo'), ('BLG', 'ShowBlog'), ('CON', 'ShowContact'), ('ITM', 'ShowItems')], default='INF', max_length=3, verbose_name='Option App')),
                ('location', models.CharField(blank=True, choices=[('NAVBAR', 'NavBar'), ('FOOTER', 'Footer')], default='NAVBAR', max_length=6, verbose_name='Option Type')),
                ('position', models.PositiveIntegerField(unique=True, verbose_name='Position')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('mainTitle', models.CharField(max_length=60, verbose_name='Main title')),
                ('imageTitle', models.ImageField(blank=True, null=True, upload_to='mainApp', verbose_name='Image title')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('style', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainApp.style', verbose_name='Style')),
            ],
            options={
                'verbose_name': 'page',
                'verbose_name_plural': 'pages',
            },
        ),
    ]
