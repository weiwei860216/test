from django.db import models
from collections import OrderedDict

# Create your models here.


class Qusetion(models.Model):
    question = models.CharField(max_length=200, blank=False, null=False)
    answer1 = models.CharField(max_length=200, blank=False, null=False)
    answer2 = models.CharField(max_length=200, blank=False, null=False)
    answer3 = models.CharField(max_length=200, blank=False, null=False)
    answer4 = models.CharField(max_length=200, blank=False, null=False)
    correct = models.CharField(max_length=7, blank=False, null=False)
    usetimes = models.IntegerField(default=0)
    correcttimes = models.IntegerField(default=0)
    record = models.ManyToManyField('Exam')

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return 'No.' + str(self.id)

    @property
    def correctrate(self):
        return self.correcttimes / self.usetimes * 100


class Exam(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    question = models.TextField(blank=True)
    usetimes = models.IntegerField(default=0)
    correcttimes = models.IntegerField(default=0)

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name

    @property
    def correctrate(self):
        return self.correcttimes / self.usetimes * 100


class ListeningQuestion(models.Model):
    audio_name = models.CharField(max_length=255, primary_key=True)
    audio_file = models.FileField(upload_to='listening/', blank=True)
    answer1 = models.CharField(max_length=255, blank=False, null=False)
    answer2 = models.CharField(max_length=255, blank=False, null=False)
    answer3 = models.CharField(max_length=255, blank=False, null=False)
    answer4 = models.CharField(max_length=255, blank=False, null=False)
    correct = models.CharField(max_length=255, blank=False, null=False)
    usetimes = models.IntegerField(default=0)
    correcttimes = models.IntegerField(default=0)
    record = models.ManyToManyField('Exam', blank=True)

    class Meta:
        ordering = ('-audio_name',)

    def __str__(self):
        return str(self.audio_name)


class User(models.Model):
    account = models.CharField(max_length=10, primary_key=True)
    password = models.CharField(max_length=10)

    class Meta:
        ordering = ('-account',)

    def __str__(self):
        return self.account


class AnswerSheet(models.Model):
    historical = models.ForeignKey('Exam', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    questions = models.TextField(blank=False, null=True)
    answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.user) + '\'s' + str(self.historical)

