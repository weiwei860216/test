# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Qusetion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('question', models.CharField(max_length=200)),
                ('answer1', models.CharField(max_length=200)),
                ('answer2', models.CharField(max_length=200)),
                ('answer3', models.CharField(max_length=200)),
                ('answer4', models.CharField(max_length=200)),
                ('correct', models.CharField(max_length=7)),
                ('usetimes', models.IntegerField(default=0)),
                ('correcttimes', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='TestBook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('usetimes', models.IntegerField(default=0)),
                ('correcttimes', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
