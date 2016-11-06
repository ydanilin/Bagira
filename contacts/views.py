from django.shortcuts import render


# Create your views here.
def post_contacts(request):
    return render(request, 'contacts/contacts.html', {})
