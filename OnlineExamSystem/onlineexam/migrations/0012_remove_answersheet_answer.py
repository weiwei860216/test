# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineexam', '0011_auto_20180924_0213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answersheet',
            name='answer',
        ),
    ]
