# Generated by Django 2.0 on 2020-04-07 03:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0021_auto_20200329_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='available_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 3, 59, 6, 843124), verbose_name='可领取时间'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='coupon_valid_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 7, 3, 59, 6, 843056), verbose_name='有效期'),
        ),
        migrations.AlterField(
            model_name='vip',
            name='vip_valid_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 7, 3, 59, 6, 842589), verbose_name='有效期'),
        ),
    ]