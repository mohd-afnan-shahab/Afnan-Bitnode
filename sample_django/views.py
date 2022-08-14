# I have created this file - AFNAN 

from django.http import HttpResponse
from django.shortcuts import render 


def index(request):
    return render(request, 'myFirst.html')   

def removepunc(request):
    djtext = request.GET.get('text', 'default')
    print(djtext) 
    return HttpResponse("remove punc") 

    # return HttpResponse("HELLO TEAM!") 

def about(request):
    return HttpResponse("<h1>About Afnan</h1>") 

def website(request):
    return HttpResponse('''<h1> Hello everyone, I'd love to share you all my codechef ID </h1> <a href = "https://www.codechef.com/users/mafnan263/edit"> Codechef Afnan Profile </a>''')   

