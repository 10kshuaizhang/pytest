# Generated by Django 2.0 on 2020-03-07 02:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0004_vip_valid_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vip',
            name='valid_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 6, 2, 25, 41, 780538), verbose_name='有效期'),
        ),
    ]
