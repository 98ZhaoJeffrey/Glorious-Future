from django.shortcuts import render
from django.shortcuts import redirect, render
from django.db.models import Q
from .models import Post
from django.contrib.auth.decorators import login_required 
from django.contrib.admin.views.decorators import staff_member_required, user_passes_test
from django.core.paginator import Paginator
# Create your views here.

def can_view_post(user):
    #only students and admins may use the search, submitForm functions
    return (not bool(user.is_staff) or user.is_superuser)

@login_required(login_url='login')
@user_passes_test(can_view_post)
def search(request):
    filterList = ['Everyone', 'Black', 'Hispanic', 'Female', 'LGBT', 'Immigrants', 'Disabled', 'Poor']
    sorts = {"Alphabetic":"thing", "Value Increasing":"", "Value Decreasing":"", "Due Date":""}
    query = request.GET.get('query', '')
    Filter = request.GET.get('filter', 'Everyone')
    sortby = request.GET.get('sortby', 'Default')
    pageNum = request.GET.get('page', '1')
    postResult = Post.objects.all()
    Filter = [Filter] if (Filter in filterList) else ['Everyone']
    if(query):
        #search for words in the title, description or organizaton name, then filter out the tags
        postResult = Post.objects.filter((Q(title__icontains=query)|Q(description__icontains=query))|Q(organization__username__icontains=query))
        #.filter(tags__name__in=Filter)

    pageObj = Paginator(postResult, 12)
    page = pageObj.page(pageNum)
    context = {
        'result': postResult,
        'page_obj': page,
        'query': query,
        'filter': Filter[0],
        'sortby': sortby
        }
    return render(request, 'search.html', context=context)

@login_required(login_url='login')
@user_passes_test(can_view_post)
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
@staff_member_required
def createPost(request):
    return render(request, 'create_post.html')

@login_required(login_url='login')
@staff_member_required
def createForm(request):
    pass