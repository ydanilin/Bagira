from django.shortcuts import render


# Create your views here.
def post_photos(request):
    return render(request, 'photos/photos.html', {})
