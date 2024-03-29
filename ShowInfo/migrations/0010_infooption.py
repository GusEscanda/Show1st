# Generated by Django 3.1.1 on 2020-11-07 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0015_option'),
        ('ShowInfo', '0009_auto_20201104_0223'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoOption',
            fields=[
                ('option_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mainApp.option')),
                ('optType', models.CharField(choices=[('NAVBAR', 'NavBar'), ('FOOTER', 'Footer')], default='NAVBAR', max_length=6, verbose_name='Option Type')),
                ('infoPage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShowInfo.infopage', verbose_name='Info Page')),
            ],
            bases=('mainApp.option',),
        ),
    ]
