# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineexam', '0012_remove_answersheet_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('name', models.CharField(primary_key=True, max_length=100, serialize=False)),
                ('usetimes', models.IntegerField(default=0)),
                ('correcttimes', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('-name',),
            },
        ),
        migrations.AlterField(
            model_name='answersheet',
            name='historical',
            field=models.ForeignKey(to='onlineexam.Exam'),
        ),
        migrations.AlterField(
            model_name='listeningquestion',
            name='record',
            field=models.ManyToManyField(blank=True, to='onlineexam.Exam'),
        ),
        migrations.AlterField(
            model_name='qusetion',
            name='record',
            field=models.ManyToManyField(to='onlineexam.Exam'),
        ),
        migrations.DeleteModel(
            name='HistoricalRecord',
        ),
    ]
