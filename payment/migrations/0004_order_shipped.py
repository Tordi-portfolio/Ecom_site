# Generated by Django 4.2.7 on 2024-12-18 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_orderitem_price_orderitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipped',
            field=models.BooleanField(default=False),
        ),
    ]