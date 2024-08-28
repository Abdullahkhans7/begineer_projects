# Generated by Django 5.1 on 2024-08-27 10:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvstream', '0002_line_items_order_line_item_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='line_items',
            name='OrderID',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Line_item_id',
        ),
        migrations.AddField(
            model_name='line_items',
            name='Order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='csvstream.order'),
        ),
    ]