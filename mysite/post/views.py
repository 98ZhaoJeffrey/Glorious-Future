from django.shortcuts import render
from django.shortcuts import redirect, render
from django.db.models import Q
from .models import Post
from django.contrib.auth.decorators import login_required 
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

@login_required(login_url='login')
def search(request):
    context = {}
    query = request.GET.get('query', '')
    Filter = request.GET.get('filter', '')
    page = request.GET.get('page', '')
    result = Post.objects.filter((Q(title__icontains=query)|Q(description__icontain=query))|Q(organization__username__icontains=query))
    context['results'] = result
    return render(request, 'search.html', context=context)

@login_required(login_url='login')
#@staff_member_required()
def createPost(request):
    return render(request, 'create_post.html')

@login_required(login_url='login')
def submitForm(request):
    context = {}
    id = request.GET.get('uuid', '')
    try:
        post = Post.objects.get(UUID=id)
        context['post'] = post
        return render(request, 'scholarship.html', context=context) 
    except:
        return redirect(search)

@login_required(login_url='login')
def createForm(request):
    pass