# Generated by Django 3.1.1 on 2020-11-30 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ShowItems', '0012_delete_shoppingcart'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCartRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartId', models.CharField(max_length=100, unique=True)),
                ('updated', models.DateTimeField()),
                ('items', models.ManyToManyField(through='ShowItems.ItemCartRelationship', to='ShowItems.Item')),
            ],
        ),
        migrations.AddField(
            model_name='itemcartrelationship',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShowItems.shoppingcart'),
        ),
        migrations.AddField(
            model_name='itemcartrelationship',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShowItems.item'),
        ),
    ]
