# Generated by Django 4.2.6 on 2023-10-28 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_orderitem_address_orderitem_pincode'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='name',
            field=models.TextField(default=False),
        ),
    ]
