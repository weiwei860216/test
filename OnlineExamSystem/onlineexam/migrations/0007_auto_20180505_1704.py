# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineexam', '0006_auto_20180503_0828'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListeningQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('audio_name', models.CharField(max_length=255)),
                ('audio_file', models.FileField(blank=True, upload_to='media/')),
                ('answer1', models.CharField(max_length=200)),
                ('answer2', models.CharField(max_length=200)),
                ('answer3', models.CharField(max_length=200)),
                ('answer4', models.CharField(max_length=200)),
                ('correct', models.CharField(max_length=7)),
                ('usetimes', models.IntegerField(default=0)),
                ('correcttimes', models.IntegerField(default=0)),
                ('record', models.ManyToManyField(to='onlineexam.HistoricalRecord')),
            ],
            options={
                'ordering': ('-audio_name',),
            },
        ),
        migrations.RemoveField(
            model_name='audio',
            name='q_id',
        ),
        migrations.DeleteModel(
            name='Audio',
        ),
    ]
