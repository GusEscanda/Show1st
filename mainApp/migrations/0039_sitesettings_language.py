# Generated by Django 3.1.1 on 2020-12-18 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0038_auto_20201217_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('es', 'Spanish')], default='en', help_text='Select the language of your Site', max_length=10, verbose_name='Site Language'),
        ),
    ]
