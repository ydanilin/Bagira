# coding=utf-8
from django.shortcuts import render


# Create your views here.
def post_coach(request):
    footerItems = [
        {'caption': 'Расписание занятий',
         'viewName': 'post_schedule'},
        {'caption': 'Турниры и соревнования',
         'viewName': ''},
        {'caption': 'Контакты',
         'viewName': 'post_contacts'},
        {'caption': 'На главную',
         'viewName': 'post_list'}
    ]
    return render(request, 'coaches/coaches.html', {'footerItems': footerItems})
