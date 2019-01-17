# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineexam', '0004_auto_20180501_0142'),
    ]

    operations = [
        migrations.AddField(
            model_name='qusetion',
            name='record',
            field=models.ManyToManyField(to='onlineexam.HistoricalRecord'),
        ),
    ]
