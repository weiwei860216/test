# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineexam', '0009_auto_20180507_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listeningquestion',
            name='answer1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='listeningquestion',
            name='answer2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='listeningquestion',
            name='answer3',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='listeningquestion',
            name='answer4',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='listeningquestion',
            name='correct',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='listeningquestion',
            name='record',
            field=models.ManyToManyField(blank=True, to='onlineexam.HistoricalRecord'),
        ),
    ]
