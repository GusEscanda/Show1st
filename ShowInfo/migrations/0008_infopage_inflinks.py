# Generated by Django 3.1.1 on 2020-11-04 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShowInfo', '0007_remove_infopage_inflinks'),
    ]

    operations = [
        migrations.AddField(
            model_name='infopage',
            name='infLinks',
            field=models.ManyToManyField(blank=True, related_name='_infopage_infLinks_+', to='ShowInfo.InfoPage', verbose_name='Additional Info Links'),
        ),
    ]
