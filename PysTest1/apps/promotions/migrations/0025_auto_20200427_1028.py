# Generated by Django 2.0 on 2020-04-27 10:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0024_auto_20200407_0423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='available_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 28, 10, 27, 59, 341897), verbose_name='可领取时间'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='coupon_valid_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 27, 10, 27, 59, 341825), verbose_name='有效期'),
        ),
        migrations.AlterField(
            model_name='vip',
            name='vip_valid_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 27, 10, 27, 59, 341309), verbose_name='有效期'),
        ),
    ]
