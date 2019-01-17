# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineexam', '0008_auto_20180505_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listeningquestion',
            name='id',
        ),
        migrations.AlterField(
            model_name='listeningquestion',
            name='audio_name',
            field=models.CharField(primary_key=True, max_length=255, serialize=False),
        ),
    ]
