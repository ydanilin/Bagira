from django.shortcuts import render


# Create your views here.
def post_schedule(request):
    return render(request, 'schedule/schedule.html', {})
