# Generated by Django 2.0 on 2020-03-07 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0002_auto_20200307_0200'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userpay',
            options={'verbose_name': '付款信息', 'verbose_name_plural': '付款信息'},
        ),
    ]