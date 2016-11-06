# coding=utf-8
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^', views.post_schedule, name='post_schedule'),
]
