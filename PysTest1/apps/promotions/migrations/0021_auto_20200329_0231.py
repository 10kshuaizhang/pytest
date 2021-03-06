# Generated by Django 2.0 on 2020-03-29 02:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0020_auto_20200329_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='available_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 30, 2, 31, 58, 380513), verbose_name='可领取时间'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='coupon_valid_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 28, 2, 31, 58, 380446), verbose_name='有效期'),
        ),
        migrations.AlterField(
            model_name='vip',
            name='vip_valid_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 28, 2, 31, 58, 380085), verbose_name='有效期'),
        ),
    ]
