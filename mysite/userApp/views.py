from django.shortcuts import render

# Create your views here.

def index(request):
    text = "hello world"
    context ={'mytext' : text, 'mytext2': text }
    return render(request, 'userApp/templates/base.html', context)