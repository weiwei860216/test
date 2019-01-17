# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineexam', '0007_auto_20180505_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listeningquestion',
            name='audio_file',
            field=models.FileField(blank=True, upload_to='listening/'),
        ),
    ]
