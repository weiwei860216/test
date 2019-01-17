import re

from django.shortcuts import render, redirect
from OnlineExamSystem.settings import LOGIN_REDIRECT_URL, LOGIN_URL
from django.contrib import auth, messages

PATTERNS = {
    "username": "[a-zA-Z0-9\._-]+",
    "password": "[a-zA-Z0-9\.!@#\$%\^&\*]+"
}


# 登入
def login(request):
    if request.method == 'POST':
        serial_number = request.POST.get('serial_number', '')
        password = request.POST.get('password', '')
        next_page = request.GET.get('next', LOGIN_REDIRECT_URL)

        try:
            for field in ['username', 'password']:
                if not re.match(PATTERNS[field], eval(field)):
                    raise AttributeError

            user = auth.authenticate(serial_number=serial_number, password=password)

            auth.login(request, user)

        except Exception:
            messages.error(request, "Invalid username or password.")
            return redirect('/')

        return redirect(next_page)

    else:
        if request.user.is_authenticated:
            return redirect('/')

        else:
            return render(request, 'login.html')


# 登出
def logout(request):
    auth.logout(request)

    return redirect(LOGIN_URL)