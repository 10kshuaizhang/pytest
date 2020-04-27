# Generated by Django 2.0 on 2020-04-27 10:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('psytests', '0015_auto_20200329_0224'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentalevaluation',
            name='avatar',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='evalPics/%Y/%m', verbose_name='测评图'),
            preserve_default=False,
        ),
    ]