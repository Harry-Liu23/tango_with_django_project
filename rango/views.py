from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'hey, ?, !, ye'}
    return render(request, 'rango/index.html', context=context_dict)
def about(request):
    context_dict = {'boldmessage':'Oi'}
    return render(request, 'rango/about.html',context=context_dict)