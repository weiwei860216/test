from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from alcpt.definitions import UserType

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, serial_number, password=None):
        """
        Creates and saves a user with the given serial number.
        """

        user = self.model(
            serial_number=serial_number,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, serial_number, password):
        """
        Creates and saves a superuser with the given serial number, password.
        """

        user = self.model(
            serial_number=serial_number,
            password=password
        )

        user.is_admin = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser):
    serial_number = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    gender = models.PositiveSmallIntegerField(blank=True, null=True)
    user_type = models.PositiveSmallIntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'serial_number'

    def get_short_name(self):
        return self.serial_number

    def get_full_name(self):
        return self.serial_number

    def has_perm(self, require_user_type: UserType):
        if require_user_type is UserType.SystemManager:
            return self.user_type is UserType.SystemManager.value[0]

        else:
            return (self.user_type & require_user_type.value[0]) > 0


class Department(models.Model):
    name = models.CharField(max_length=10, primary_key=True)


class Squadron(models.Model):
    name = models.CharField(max_length=10, primary_key=True)


class Student(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE)
    department = models.ForeignKey("Department", on_delete=models.PROTECT, blank=True)
    grade = models.PositiveSmallIntegerField(default=0)
    squadron = models.ForeignKey("Squadron", on_delete=models.PROTECT, blank=True)


# 試卷
class TestPaper(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    question = models.TextField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey("User", on_delete=models.PROTECT)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# 模擬考
class Exam(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    question = models.TextField(blank=True)
    usetimes = models.IntegerField(default=0)
    correcttimes = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('User', on_delete=models.PROTECT)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-create_time',)

    def __str__(self):
        return self.name

    @property
    def correctrate(self):
        return self.correcttimes / self.usetimes * 100


# 題目
class Question(models.Model):
    question_type = models.PositiveSmallIntegerField()
    question_file = models.FileField(upload_to='listening/', blank=True, null=True)
    question = models.TextField()
    option = models.TextField()
    answer = models.PositiveSmallIntegerField()
    use_time = models.IntegerField(default=0)
    correct_time = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('User', on_delete=models.PROTECT)
    update_time = models.DateTimeField(auto_now=True)
    last_updated_by = models.ForeignKey('User', on_delete=models.SET_NULL, blank=True, null=True)
    enable = models.BooleanField(default=False)
    used_to = models.ManyToManyField(Exam)
    
    class Meta:
        ordering = ('-question',)

    @property
    def correct_rate(self):
        return self.correct_time / self.use_time * 100


# 答案卷
class AnswerSheet(models.Model):
    exam = models.ForeignKey('Exam', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    questions = models.TextField(blank=False, null=True)
    answer = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    score = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.user) + '\'s' + str(self.exam)


# 受測名單
class Group(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    member = models.ManyToManyField('Student', blank=True)

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name


# 公告
class Proclamation(models.Model):
    title = models.TextField(max_length=255)
    text = models.TextField(max_length=512)
    enable = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-create',)

    def __str__(self):
        return self.title