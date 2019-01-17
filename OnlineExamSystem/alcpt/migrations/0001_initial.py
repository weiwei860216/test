# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConversationQuestion',
            fields=[
                ('answer1', models.CharField(max_length=255)),
                ('answer2', models.CharField(max_length=255)),
                ('answer3', models.CharField(max_length=255)),
                ('answer4', models.CharField(max_length=255)),
                ('correct', models.CharField(max_length=255)),
                ('usetimes', models.IntegerField(default=0)),
                ('correcttimes', models.IntegerField(default=0)),
                ('enable', models.BooleanField(default=False)),
                ('audio_name', models.CharField(primary_key=True, max_length=255, serialize=False)),
                ('audio_file', models.FileField(upload_to='conversation/')),
            ],
            options={
                'ordering': ('-audio_name',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GrammerQuestion',
            fields=[
                ('answer1', models.CharField(max_length=255)),
                ('answer2', models.CharField(max_length=255)),
                ('answer3', models.CharField(max_length=255)),
                ('answer4', models.CharField(max_length=255)),
                ('correct', models.CharField(max_length=255)),
                ('usetimes', models.IntegerField(default=0)),
                ('correcttimes', models.IntegerField(default=0)),
                ('enable', models.BooleanField(default=False)),
                ('question', models.CharField(primary_key=True, max_length=255, serialize=False)),
            ],
            options={
                'ordering': ('-question',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('name', models.CharField(primary_key=True, max_length=255, serialize=False)),
            ],
            options={
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='ListeningQuestion',
            fields=[
                ('answer1', models.CharField(max_length=255)),
                ('answer2', models.CharField(max_length=255)),
                ('answer3', models.CharField(max_length=255)),
                ('answer4', models.CharField(max_length=255)),
                ('correct', models.CharField(max_length=255)),
                ('usetimes', models.IntegerField(default=0)),
                ('correcttimes', models.IntegerField(default=0)),
                ('enable', models.BooleanField(default=False)),
                ('audio_name', models.CharField(primary_key=True, max_length=255, serialize=False)),
                ('audio_file', models.FileField(upload_to='listening/')),
            ],
            options={
                'ordering': ('-audio_name',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Proclamation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.TextField(max_length=255)),
                ('text', models.TextField(max_length=512)),
                ('enable', models.BooleanField(default=False)),
                ('create', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-create',),
            },
        ),
        migrations.CreateModel(
            name='ReadingQuestion',
            fields=[
                ('answer1', models.CharField(max_length=255)),
                ('answer2', models.CharField(max_length=255)),
                ('answer3', models.CharField(max_length=255)),
                ('answer4', models.CharField(max_length=255)),
                ('correct', models.CharField(max_length=255)),
                ('usetimes', models.IntegerField(default=0)),
                ('correcttimes', models.IntegerField(default=0)),
                ('enable', models.BooleanField(default=False)),
                ('question', models.CharField(primary_key=True, max_length=255, serialize=False)),
            ],
            options={
                'ordering': ('-question',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('exam_date', models.DateTimeField(primary_key=True, serialize=False, auto_now=True)),
                ('error', models.CharField(max_length=100)),
                ('score', models.IntegerField()),
            ],
            options={
                'ordering': ('-tester',),
            },
        ),
        migrations.CreateModel(
            name='TestPaper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('question', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('student_id', models.CharField(primary_key=True, max_length=10, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=4)),
                ('sex', models.CharField(max_length=1, choices=[('0', '男'), ('1', '女')])),
                ('authority', models.CharField(max_length=6)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-student_id',),
            },
        ),
        migrations.CreateModel(
            name='VocabularyQuestion',
            fields=[
                ('answer1', models.CharField(max_length=255)),
                ('answer2', models.CharField(max_length=255)),
                ('answer3', models.CharField(max_length=255)),
                ('answer4', models.CharField(max_length=255)),
                ('correct', models.CharField(max_length=255)),
                ('usetimes', models.IntegerField(default=0)),
                ('correcttimes', models.IntegerField(default=0)),
                ('enable', models.BooleanField(default=False)),
                ('question', models.CharField(primary_key=True, max_length=255, serialize=False)),
            ],
            options={
                'ordering': ('-question',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExamAdmin',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to='alcpt.UserProfile')),
            ],
            options={
                'ordering': ('-user',),
            },
        ),
        migrations.CreateModel(
            name='QuestionAdmin',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to='alcpt.UserProfile')),
            ],
            options={
                'ordering': ('-user',),
            },
        ),
        migrations.CreateModel(
            name='QuestionOperator',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to='alcpt.UserProfile')),
            ],
            options={
                'ordering': ('-user',),
            },
        ),
        migrations.CreateModel(
            name='ScoreViewer',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to='alcpt.UserProfile')),
            ],
            options={
                'ordering': ('-user',),
            },
        ),
        migrations.CreateModel(
            name='SystemAdmin',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to='alcpt.UserProfile')),
            ],
            options={
                'ordering': ('-user',),
            },
        ),
        migrations.CreateModel(
            name='Tester',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, related_name='tester', to='alcpt.UserProfile')),
                ('_class', models.CharField(max_length=3)),
                ('major', models.CharField(max_length=1)),
                ('squadron', models.CharField(max_length=1)),
                ('record', models.ManyToManyField(blank=True, related_name='record', to='alcpt.Score')),
            ],
            options={
                'ordering': ('-user',),
            },
        ),
        migrations.AddField(
            model_name='vocabularyquestion',
            name='adder_by_QA',
            field=models.ForeignKey(blank=True, related_name='VQ_from_QA', to='alcpt.QuestionAdmin'),
        ),
        migrations.AddField(
            model_name='vocabularyquestion',
            name='adder_by_QO',
            field=models.ForeignKey(blank=True, related_name='VQ_from_QO', to='alcpt.QuestionOperator'),
        ),
        migrations.AddField(
            model_name='score',
            name='tester',
            field=models.ForeignKey(related_name='tester', to='alcpt.Tester'),
        ),
        migrations.AddField(
            model_name='readingquestion',
            name='adder_by_QA',
            field=models.ForeignKey(blank=True, related_name='RQ_from_QA', to='alcpt.QuestionAdmin'),
        ),
        migrations.AddField(
            model_name='readingquestion',
            name='adder_by_QO',
            field=models.ForeignKey(blank=True, related_name='RQ_from_QO', to='alcpt.QuestionOperator'),
        ),
        migrations.AddField(
            model_name='listeningquestion',
            name='adder_by_QA',
            field=models.ForeignKey(blank=True, related_name='LQ_from_QA', to='alcpt.QuestionAdmin'),
        ),
        migrations.AddField(
            model_name='listeningquestion',
            name='adder_by_QO',
            field=models.ForeignKey(blank=True, related_name='LQ_from_QO', to='alcpt.QuestionOperator'),
        ),
        migrations.AddField(
            model_name='group',
            name='member',
            field=models.ManyToManyField(blank=True, to='alcpt.Tester'),
        ),
        migrations.AddField(
            model_name='grammerquestion',
            name='adder_by_QA',
            field=models.ForeignKey(blank=True, related_name='GQ_from_QA', to='alcpt.QuestionAdmin'),
        ),
        migrations.AddField(
            model_name='grammerquestion',
            name='adder_by_QO',
            field=models.ForeignKey(blank=True, related_name='GQ_from_QO', to='alcpt.QuestionOperator'),
        ),
        migrations.AddField(
            model_name='conversationquestion',
            name='adder_by_QA',
            field=models.ForeignKey(blank=True, related_name='CQ_from_QA', to='alcpt.QuestionAdmin'),
        ),
        migrations.AddField(
            model_name='conversationquestion',
            name='adder_by_QO',
            field=models.ForeignKey(blank=True, related_name='CQ_from_QO', to='alcpt.QuestionOperator'),
        ),
    ]
