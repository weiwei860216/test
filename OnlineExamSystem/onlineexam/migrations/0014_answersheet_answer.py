# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineexam', '0013_auto_20181004_0214'),
    ]

    operations = [
        migrations.AddField(
            model_name='answersheet',
            name='answer',
            field=models.TextField(null=True),
        ),
    ]
