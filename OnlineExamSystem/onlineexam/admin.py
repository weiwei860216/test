from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(AnswerSheet)
admin.site.register(Qusetion)
admin.site.register(Exam)
admin.site.register(ListeningQuestion)
