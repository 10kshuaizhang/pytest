# Generated by Django 2.0 on 2020-03-07 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_delete_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_vip',
            field=models.BooleanField(default=False, verbose_name='会员状态'),
        ),
    ]
