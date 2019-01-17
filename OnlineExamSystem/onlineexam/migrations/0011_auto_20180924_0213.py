# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineexam', '0010_auto_20180902_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerSheet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('answer', models.CharField(max_length=1024)),
                ('historical', models.ForeignKey(to='onlineexam.HistoricalRecord')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('account', models.CharField(primary_key=True, max_length=10, serialize=False)),
                ('password', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ('-account',),
            },
        ),
        migrations.AddField(
            model_name='answersheet',
            name='user',
            field=models.ForeignKey(to='onlineexam.User'),
        ),
    ]
