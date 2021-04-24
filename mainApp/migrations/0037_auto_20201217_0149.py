# Generated by Django 3.1.1 on 2020-12-17 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0036_auto_20201210_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='app',
            field=models.CharField(choices=[('HOM', 'Home'), ('INF', 'ShowInfo'), ('BLG', 'ShowBlog'), ('CON', 'ShowContact'), ('ITM', 'ShowItems')], help_text='The App determines the type of information you will show in this menu option of the site', max_length=3, verbose_name='Option App'),
        ),
        migrations.AlterField(
            model_name='page',
            name='homeImage',
            field=models.ImageField(blank=True, help_text='If loaded, the image that will link to this menu option in the home page', null=True, upload_to='mainApp', verbose_name='Home Page Image'),
        ),
        migrations.AlterField(
            model_name='page',
            name='imageTitle',
            field=models.ImageField(blank=True, help_text='Load an image if you want to replace the main title with a banner', null=True, upload_to='mainApp', verbose_name='Image title'),
        ),
        migrations.AlterField(
            model_name='page',
            name='location',
            field=models.CharField(blank=True, choices=[('NAVBAR', 'NavBar'), ('FOOTER', 'Footer')], help_text='Select where the link to this information will be located: in the nav bar, in the footer or in the body of another page', max_length=6, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='page',
            name='mainTitle',
            field=models.CharField(help_text='Main title to be displayed at the top of the page', max_length=60, verbose_name='Main title'),
        ),
        migrations.AlterField(
            model_name='page',
            name='name',
            field=models.CharField(help_text='The name of this page', max_length=30, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='page',
            name='position',
            field=models.PositiveIntegerField(help_text='Any numeric value. The menu options / footer links will be displayed ordered by this value, but the value itself will not be displayed.', unique=True, verbose_name='Position'),
        ),
        migrations.AlterField(
            model_name='page',
            name='style',
            field=models.ForeignKey(blank=True, help_text='Select a Style for this menu option or information page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pages', to='mainApp.style', verbose_name='Style'),
        ),
    ]