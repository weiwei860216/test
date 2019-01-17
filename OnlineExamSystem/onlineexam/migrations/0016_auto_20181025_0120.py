# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineexam', '0015_exam_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='answersheet',
            name='questions',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='answersheet',
            name='answer',
            field=models.TextField(blank=True, null=True),
        ),
    ]
