# Generated by Django 3.1.1 on 2020-12-17 22:59

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('ShowContact', '0013_auto_20201217_1959'),
        ('ShowItems', '0020_auto_20201210_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='categs',
            field=models.ManyToManyField(help_text='Select all the categories that this item belongs to.', related_name='items', to='ShowItems.ItemCategory', verbose_name='Categories'),
        ),
        migrations.AlterField(
            model_name='item',
            name='code',
            field=models.CharField(db_index=True, help_text='The code that identifies the item', max_length=20, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='item',
            name='descrip',
            field=models.TextField(blank=True, help_text='Description of the item as you want to appear in the site', verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, help_text='Large detailed image of the item, designed to cover almost the entire screen', null=True, upload_to='ShowItems', verbose_name='Detailed Image'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(help_text='Short name of the item', max_length=60, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='item',
            name='thumb',
            field=models.ImageField(help_text='Thumbnail image that will appear in the items grid.', upload_to='ShowItems', verbose_name='Thumbnail image'),
        ),
        migrations.AlterField(
            model_name='itemcategory',
            name='name',
            field=models.CharField(help_text='Create categories and later assign your items to one or many the them.', max_length=30, unique=True, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='itemspage',
            name='enableShopCart',
            field=models.BooleanField(default=False, help_text='Allow user to add/remove items to a Shopping Cart and later send you an inquiry email attaching the list.', verbose_name='Enable Shopping Cart'),
        ),
        migrations.AlterField(
            model_name='itemspage',
            name='footText',
            field=tinymce.models.HTMLField(blank=True, help_text='Enter text to be displayed after the items grid (optional)', null=True, verbose_name='Posterior text'),
        ),
        migrations.AlterField(
            model_name='itemspage',
            name='headerText',
            field=tinymce.models.HTMLField(blank=True, help_text='Enter text to be displayed before the items grid (optional)', null=True, verbose_name='Previous text'),
        ),
        migrations.AlterField(
            model_name='itemspage',
            name='pageCatFilter',
            field=models.ForeignKey(blank=True, help_text='Display only the items that are in the selected category. If none is selected, displays all.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='ShowItems.itemcategory', verbose_name='Filter Category'),
        ),
        migrations.AlterField(
            model_name='itemspage',
            name='sendCartPage',
            field=models.ForeignKey(blank=True, help_text='Select the Contact Page that will be displayed to allow the user to complete and send the inquiry email.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='itemPages', to='ShowContact.contactpage', verbose_name='Send Cart Page'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='cartId',
            field=models.CharField(help_text='uuid4 code stored in the session to maintain a separate Shopping Cart for each user browsing the site', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='items',
            field=models.ManyToManyField(help_text='The items list of the Cart', to='ShowItems.Item'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='updated',
            field=models.DateTimeField(auto_now=True, help_text='Last update date, used to automatically clean the unused (abandoned) carts'),
        ),
    ]