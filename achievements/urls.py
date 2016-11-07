# coding=utf-8
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_achievements, name='post_achievements'),
]
