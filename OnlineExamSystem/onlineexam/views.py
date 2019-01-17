from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from collections import OrderedDict
from .models import *
from .forms import *
import random
import json

# Create your views here.


# 建立試卷(選項打亂, 隨機選題)
# def create(request):
#     listening_picked = random.sample(list(ListeningQuestion.objects.all()), 2)
#     rec = HistoricalRecord.objects.create()
#     for obj in listening_picked:
#         obj.record.add(rec.id)
#         obj.save()
#     q_list = [que.audio_name for que in listening_picked]
#     ans_list = [[q.answer1, q.answer2, q.answer3, q.answer4] for q in listening_picked]
#     for ans in ans_list:
#         random.shuffle(ans)
#     questiondir = {que: ans for que, ans in zip(q_list, ans_list)}
#
#     return render(request, 'exam1.html', {'q_dir': questiondir})


# 建立試卷(打亂試卷順序)
# def exam1(request):
#     exam1 = Exam.objects.get(name='Test!!!')
#     questions = json.loads(exam1.question)
#     random.shuffle(questions)
#     question_picked = [ListeningQuestion.objects.get(audio_name=name) for name in questions]
#     q_list = [que.audio_name for que in question_picked]
#     ans_list = [{'1': q.answer1, '2': q.answer2, '3': q.answer3, '4': q.answer4} for q in question_picked]
#     cor_list = [que.correct for que in question_picked]
#     for count in range(len(ans_list)):
#         keys = [key for key in ans_list[count].keys()]
#         random.shuffle(keys)
#         random_ans_dir = OrderedDict()
#         for key in keys:
#             random_ans_dir[key] = ans_list[count][key]
#
#         ans_list[count] = random_ans_dir
#
#     questiondir = {que: ans for que, ans in zip(q_list, ans_list)}
#     correctdir = {que: cor for que, cor in zip(q_list, cor_list)}
#
#     if request.method == 'POST':
#         for obj in question_picked:
#             obj.usetimes += 1
#             obj.save()
#         copy_querydict = request.POST.copy()
#         copy_querydict.pop('csrfmiddlewaretoken')
#         keys = copy_querydict.keys()
#         answer = OrderedDict()
#         score = 0
#         for key in keys:
#             answer[key] = request.POST[key]
#             if request.POST[key] == correctdir[key]:
#                 score += 1
#         user = request.session['account']
#         sheet = AnswerSheet.objects.create(historical=questions,
#                                            user=User.objects.get(account=user),
#                                            answer=json.dumps(answer))
#         data = {
#             'exam1': questions.name,
#             'score': score,
#             'user': user,
#             'cor': correctdir,
#             'answer': answer,
#         }
#
#         return render(request, 'comparison.html', data)
#
#     return render(request, 'exam1.html', locals())

def exam1(request):
    exam = Exam.objects.get(name='Test!!!')
    questions = json.loads(exam.question.replace('\'', ''))
    random.shuffle(questions)
    question_picked = [ListeningQuestion.objects.get(audio_name=name) for name in questions]
    q_list = [que.audio_name for que in question_picked]
    ans_list = [{'1': q.answer1, '2': q.answer2, '3': q.answer3, '4': q.answer4} for q in question_picked]
    cor_list = [que.correct for que in question_picked]
    for count in range(len(ans_list)):
        keys = [key for key in ans_list[count].keys()]
        random.shuffle(keys)
        random_ans_dir = OrderedDict()
        for key in keys:
            random_ans_dir[key] = ans_list[count][key]

        ans_list[count] = random_ans_dir

    questiondir = {que: ans for que, ans in zip(q_list, ans_list)}
    correctdir = {que: cor for que, cor in zip(q_list, cor_list)}
    ans_sheet = AnswerSheet.objects.create(historical=exam,
                                           user=User.objects.get(account=request.session['account']),
                                           questions=json.dumps(questiondir))

    return render(request, 'exam.html', locals())

# 上傳文法題
def upload(request):
    return render(request, 'upload.html')


# 聽力題目列
def listening_question_list(request):
    lq_list = list(ListeningQuestion.objects.all())

    return render(request, 'listening_question_list.html', {'lq_list': lq_list})


# 聽力題目表
def listening_question_profile(request, audio_name):
    question = ListeningQuestion.objects.get(audio_name=audio_name)
    form = ModifyListenQuestionForm(instance=question)

    return render(request, 'listening_question.html', locals())


# 建立聽力題目
def upload_listening_question(request):
    error = ''
    if request.method == 'POST':
        form = UploadListenQuestionForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            audio_file = data['audio_file']
            audio_name = audio_file.name[:-4:]
            answer1 = data['answer1']
            answer2 = data['answer2']
            answer3 = data['answer3']
            answer4 = data['answer4']
            correct = data['correct']
            if ListeningQuestion.objects.all().filter(audio_name=audio_name):
                error = '題目已存在'

            else:
                ListeningQuestion.objects.create(audio_file=audio_file, audio_name=audio_name, answer1=answer1,
                                                 answer2=answer2, answer3=answer3, answer4=answer4, correct=correct)
                return HttpResponseRedirect('/upload/')

        else:
            error = '請確認沒有空的欄位'

    else:
        form = UploadListenQuestionForm()

    return render(request, 'upload_listening_question.html', {'error': error, 'form': form})


# 考古題表
def historical_list(request):
    account = request.session['account']
    h_list = AnswerSheet.objects.filter(user=account)
    answer_list = json.loads(AnswerSheet.objects.get(user=account, historical='Test!!!').answer)

    return render(request, 'historical_list.html', locals())


# 考古題題目
def historical_profile(request, name):
    account = request.session['account']
    question_list = [question for question in Exam.objects.get(name=name).listeningquestion_set.all()]
    answer_list = [[q.answer1, q.answer2, q.answer3, q.answer4, q.correct] for q, ans in question_list]
    question_dir = {que: ans for que, ans in zip(question_list, answer_list)}

    return render(request, 'historical_profile.html', {'q_dir': question_dir})


# 登入
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            account = data['account']
            password = data['password']
            user = User.objects.get(account=account, password=password)
            if user:
                request.session['account'] = user.account
                return render(request, 'home.html', locals())

            else:
                error = 'User not exist!'

        else:
            error = 'Field not full!'

    else:
        form = LoginForm()

    return render(request, 'login.html', locals())


# 首頁
def home(request):
    if request.session['account']:
        account = request.session['account']
    else:
        account = 'False'
    # session = request.session.keys()
    return render(request, 'home.html', locals())


# 交卷
def comparison(request):
    ans_sheet = AnswerSheet.objects.get(id=request.POST['ans-id'])
    copy_querydict = request.POST.copy()
    copy_querydict.pop('csrfmiddlewaretoken')
    copy_querydict.pop('ans-id')
    keys = copy_querydict.keys()
    answer = OrderedDict()
    score = 0
    for key in keys:
        answer[key] = request.POST[key]
        if request.POST[key] == ListeningQuestion.objects.get(audio_name=key).correct:
                    score += 1

    ans_sheet.answer = json.dumps(answer)
    ans_sheet.save()
    return render(request, 'comparison.html', locals())


# 使用者考試歷史紀錄
def user_historical(request):
    u_h_list = Exam.objects.all().order_by('-id')

    return render(request, 'historical_list.html', locals())