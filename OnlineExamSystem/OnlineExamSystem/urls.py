"""OnlineExamSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from onlineexam import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', views.login, name='login'),
    url(r'^home/$', views.home, name='home'),
    url(r'^exam1/$', views.exam1, name='exam1'),
    url(r'^comparison/$', views.comparison, name='comparison'),
    url(r'^listening_question_list/$', views.listening_question_list, name='lq_list'),
    url(r'^listening_question_profile=(?P<id>\w+)/$', views.listening_question_profile, name='lq_profile'),
    url(r'^historical_list/$', views.historical_list, name='h_list'),
    url(r'^historical_profile=(?P<id>\w+)/$', views.historical_profile, name='h_profile'),
    url(r'^upload/listening/$', views.upload_listening_question, name='upload_listening'),
    url(r'^upload/$', views.upload, name='upload'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
