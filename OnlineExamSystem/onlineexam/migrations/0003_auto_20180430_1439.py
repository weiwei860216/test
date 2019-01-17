# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineexam', '0002_testbook_questions'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('usetimes', models.IntegerField(default=0)),
                ('correcttimes', models.IntegerField(default=0)),
                ('questions', models.ForeignKey(to='onlineexam.Qusetion')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.DeleteModel(
            name='TestBook',
        ),
    ]
