# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineexam', '0014_answersheet_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam1',
            name='question',
            field=models.TextField(blank=True),
        ),
    ]
