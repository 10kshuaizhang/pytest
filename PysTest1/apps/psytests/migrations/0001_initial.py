# Generated by Django 2.0 on 2020-02-24 13:10

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MentalEvaluation',
            fields=[
                ('eval_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('eval_type', multiselectfield.db.fields.MultiSelectField(choices=[('type1', 'intro1'), ('type2', 'intro2'), ('type3', 'intro3')], max_length=17)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('intro', models.TextField()),
                ('price', models.CharField(max_length=20)),
                ('created_on', models.CharField(max_length=200)),
                ('is_online', models.CharField(choices=[(1, 'Online'), (2, 'Offline'), (3, 'In Progress')], max_length=30)),
                ('avatar', models.CharField(max_length=200)),
                ('nums_eval', models.IntegerField()),
                ('state', models.IntegerField()),
                ('ques_num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserEvaluation',
            fields=[
                ('user_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('eval_id', models.CharField(max_length=200)),
                ('eval_score', models.IntegerField()),
                ('user_count', models.IntegerField()),
                ('eval_result', models.CharField(max_length=100)),
                ('created_on', models.CharField(max_length=200)),
                ('payment_status', models.CharField(choices=[('paid', 'paid'), ('not paid', 'not paid')], max_length=20)),
                ('mentalEvaluation', models.ManyToManyField(to='psytests.MentalEvaluation')),
            ],
        ),
        migrations.CreateModel(
            name='UserReviewForEvaluation',
            fields=[
                ('eval_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=200)),
                ('review', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
