from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage' : 'All your contacts in one place!'}
    return render(request, 'contactsapp/index.html', context=context_dict)

def about(request):
    return HttpResponse("Contacts App for Assignment <br/> <a href='/contacts/'>Index</a>")