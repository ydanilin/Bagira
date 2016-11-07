# coding=utf-8
from django.shortcuts import render


# Create your views here.
def post_achievements(request):
    return render(request, 'achievements/achievements.html', {})
