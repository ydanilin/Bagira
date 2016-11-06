# coding=utf-8
from django.shortcuts import render


# Create your views here.
def post_coach(request):
    return render(request, 'coaches/coaches.html', {})
