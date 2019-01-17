import re

from django.shortcuts import render, redirect
from OnlineExamSystem.settings import LOGIN_REDIRECT_URL, LOGIN_URL
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .models import *
from .decorators import permission_check


# 系統管理員首頁
@permission_check(UserType.SystemManager)
def sm_home(request):
    user = User.objects.all().order_by('-updated')[:10]  # 顯示近十筆更新的資料
    if 'username' in request.session:
        username = request.session['username']
    return render(request, 'manage/sa_home.html', locals())


# 系統管理員新增使用者頁面
@permission_check(UserType.SystemManager)
@require_http_methods(["GET", "POST"])
def sm_create(request):
    if request.method == 'POST':
        account = request.POST.get('account')
        if not re.match('[a-z0-9]+', account):
            messages.error(request, 'Invalid account.Account can only contain letters and numbers.')

        user_type_value = 0
        if request.user.has_perm(UserType.SystemManager):
            i = 0
            for user_type in UserType.__member__.values():
                if user_type and request.POST.get('user_type_{}'.format(i)):
                    user_type_value |= user_type.values[0]

        else:
            user_type_value = UserType.Tester.value[0]

        if User.objects.get(serial_number=account):
            messages.error(request, 'User "{}" has existed.')

        else:
            new_user = User.objects.create(serial_number=account,
                                           user_type=user_type_value,
                                           password=account)

            if new_user.has_perm(UserType.Tester):
                Student.objects.create(user=new_user)

        messages.success(request, 'Create user "{}" sucessfull.'.format(account))

        return redirect('/user')

    else:
        data = {'user_type': UserType.__members__}

        return render(request, 'manage/user/create.html', data)


# 系統管理員修改使用者資料頁面(列出所有使用者)
@permission_check(UserType.SystemManager)
def sm_update_list(request):
    user = User.objects.all().order_by('-student_id')
    if 'username' in request.session:
        username = request.session['username']
    return render(request, 'manage/update.html', {'user': user, 'username': username})


# 系統管理員修改使用者資料頁面(修改使用者資料)
@permission_check(UserType.SystemManager)
def sa_update_detail(request, serial_number):
    if request.user.serial_number != serial_number:
        if request.user.has_perm(UserType.SystemManager):
            try:
                edited_user = User.objects.get(serial_number=serial_number)

            except Exception:
                messages.error('Can\'t find user whose serial number:{}'.format(serial_number))

        else:
            messages.warning('Permission not enough.')

    else:
        user = request.user

    if request.method == 'POST':

