# Generated by Django 4.0.6 on 2022-08-04 14:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2022, 8, 4, 14, 23, 32, 821334, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
