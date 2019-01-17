# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineexam', '0005_qusetion_record'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('q_id', models.OneToOneField(primary_key=True, serialize=False, to='onlineexam.Qusetion')),
                ('audio_name', models.CharField(max_length=255)),
                ('audio_file', models.FileField(blank=True, upload_to='media/')),
            ],
            options={
                'ordering': ('-audio_name',),
            },
        ),
        migrations.RemoveField(
            model_name='historicaltestquestion',
            name='question',
        ),
        migrations.RemoveField(
            model_name='historicaltestquestion',
            name='record',
        ),
        migrations.DeleteModel(
            name='HistoricalTestQuestion',
        ),
    ]
