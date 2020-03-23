# Generated by Django 2.0 on 2020-03-06 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='coupon_type',
            field=models.CharField(choices=[('default', '默认'), ('holiday', '节日'), ('others', '其他')], default='default', max_length=20, verbose_name='优惠券类型'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='get_condition',
            field=models.CharField(choices=[('new_user', '新用户'), ('non_vip', '非会员'), ('vip', '会员')], default='non_vip', max_length=20, verbose_name='获得条件'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='get_type',
            field=models.CharField(choices=[('push', '推送'), ('pull', '领取')], default='push', max_length=20, verbose_name='获得方式'),
        ),
    ]