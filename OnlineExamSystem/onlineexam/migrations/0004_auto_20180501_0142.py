# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineexam', '0003_auto_20180430_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalTestQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('question', models.ForeignKey(to='onlineexam.Qusetion')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.RemoveField(
            model_name='historicalrecord',
            name='questions',
        ),
        migrations.AddField(
            model_name='historicaltestquestion',
            name='record',
            field=models.ForeignKey(to='onlineexam.HistoricalRecord'),
        ),
    ]
