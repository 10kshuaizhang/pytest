# Generated by Django 2.0 on 2020-03-10 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_userprofile_is_vip'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='image',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='nick_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='password',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='username',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.CharField(default='', max_length=50, verbose_name='微信城市'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='country',
            field=models.CharField(default='', max_length=50, verbose_name='微信国家'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='headimgurl',
            field=models.CharField(default='', max_length=200, verbose_name='微信头像'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='nickname',
            field=models.CharField(default='', max_length=256, verbose_name='微信昵称'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='openid',
            field=models.CharField(default='', max_length=32, verbose_name='微信 openid'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='privilege',
            field=models.CharField(default='', max_length=3, verbose_name='微信权限'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='province',
            field=models.CharField(default='', max_length=50, verbose_name='微信省份'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='refresh_token',
            field=models.CharField(default='', max_length=512, verbose_name='微信 refresh_token'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='refresh_token_time',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='unionid',
            field=models.CharField(default='', max_length=32, verbose_name='微信 unionid'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='wsex',
            field=models.CharField(default='', max_length=3, verbose_name='微信性别'),
        ),
    ]