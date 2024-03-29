# Generated by Django 3.1.1 on 2020-11-26 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShowContact', '0007_auto_20201125_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailHostConfig',
            fields=[
                ('configId', models.PositiveIntegerField(default=1, primary_key=True, serialize=False)),
                ('emailHostUser', models.CharField(blank=True, default='', max_length=100)),
                ('emailHostPassword', models.CharField(blank=True, default='', max_length=50)),
                ('emailHost', models.CharField(blank=True, default='', max_length=100)),
                ('emailPort', models.PositiveIntegerField(blank=True, default=587)),
                ('emailUseTLS', models.BooleanField()),
                ('emailUseSSL', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='socialmediaoption',
            name='code',
            field=models.CharField(max_length=50, unique=True, verbose_name='Social media code'),
        ),
    ]
