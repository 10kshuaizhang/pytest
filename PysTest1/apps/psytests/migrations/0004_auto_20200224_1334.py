# Generated by Django 2.0 on 2020-02-24 13:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psytests', '0003_auto_20200224_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreviewforevaluation',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
