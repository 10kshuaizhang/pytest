# Generated by Django 2.0 on 2020-03-23 12:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0010_auto_20200323_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vip',
            name='valid_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 22, 12, 11, 55, 312426), verbose_name='有效期'),
        ),
    ]