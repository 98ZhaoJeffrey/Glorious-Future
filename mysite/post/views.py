from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect, render
from django.db.models import Q
from .models import Post, Form, Response
from .forms import PostForm, QuestionFormForm
from django.contrib.auth.decorators import login_required 
from django.contrib.admin.views.decorators import staff_member_required, user_passes_test
from django.core.paginator import Paginator
from django.contrib import messages
import csv
from userApp.models import *
# Create your views here.

def can_view_post(user):
    #only students and admins may use the search, submitForm functions
    return (not bool(user.is_staff) or user.is_superuser)

@login_required(login_url='login')
@user_passes_test(can_view_post)
def search(request):
    filterList = ['everyone', 'black', 'hispanic', 'female', 'lgbt', 'immigrants', 'disabled', 'poor']
    sorts = {"Title(A-Z)":"title", "Title(Z-A)":"-title", "Value Increasing":"value", "Value Decreasing":"-value", "Due Date":"dueDate"}

    #urls agruments
    query = request.GET.get('query', '')
    Filter = request.GET.get('filter', 'Default')
    sortby = request.GET.get('sortby', 'Default')
    pageNum = request.GET.get('page', '1')
    
    postResult = Post.objects.all().order_by(sorts.get(sortby,"UUID"))

    if(query):
        #search for words in the title, description or organizaton name, then filter out the tags
        postResult = Post.objects.filter((Q(title__icontains=query)|Q(description__icontains=query))|Q(organization__username__icontains=query))
    if(Filter !='Default' and Filter.lower() in filterList):    
        #check if the filter the user entered is a tag
        postResult = postResult.filter(tags__name__in=[Filter.lower()]) 

    #function to help divide our query into groups of 12 for pagination
    pageObj = Paginator(postResult, 12)

    #select the page that we want
    page = pageObj.page(pageNum)


    context = {
        'result': postResult,
        'page_obj': page,
        'query': query,
        'filter': Filter,
        'sortby': sortby,
        }
    return render(request, 'search.html', context=context)

@login_required(login_url='login')
@user_passes_test(can_view_post)
def submitForm(request,formcode=None):
    if formcode:
        #save the answer form response    
        if request.method == 'POST':
            answer1 = request.POST.get('answer1', '')
            answer2 = request.POST.get('answer2', '')
            answer3 = request.POST.get('answer3', '')
            user = request.user
            
            #users can only submit one form for each scholarship
            if len(Response.objects.filter(user_id=user, form_id=formcode)) == 0:            
                form = Response(answer1=answer1, answer2=answer2, answer3=answer3, user=user, form_id=formcode)
                form.save()
                return render(request,'success.html')
            return render(request, 'error.html')
        
        #Get both the questionform and the postform to display onto the response page
        questionForm = get_object_or_404(Form,UUID=formcode)
        postForm = Post.objects.filter(Q(link__icontains=formcode))[0]
        context = {'form': questionForm, 'UUID': formcode, 'post': postForm}
        return render(request, 'response.html', context=context) 
    else:
        return redirect(search)

@login_required(login_url='login')
@staff_member_required
def createPost(request):

    #save the organization's post
    if request.method == 'POST':
        form = PostForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            filterList = ['everyone', 'black', 'hispanic', 'female', 'lgbt', 'immigrants', 'disabled', 'poor']    
            newpost = form.save()

            tags = form.cleaned_data.get('tags')
            tags = [tag.lower() for tag in tags if tag.lower() in filterList]

            newpost.tags.add(*tags)
            messages.success(request, 'You have successful created the post')
            form = PostForm(request.user)
            context = {'form':form}  
            return render(request, 'create_post.html', context=context)
        
    #form to fill out for the post
    form = PostForm(request.user)
    context = {'form':form}    
    return render(request, 'create_post.html', context=context)


@login_required(login_url='login')
@staff_member_required
def createForm(request):
    if request.method == 'POST':
        form = QuestionFormForm(request.POST)
        if form.is_valid():
            #return the uuid so the organization can use that link in the post to connect to the questionform
            formID = form.save().UUID
            messages.success(request, 'You have made your question form accessible at: ' + request.build_absolute_uri('/post/') + f'apply/{formID}')
            context = {'form': form}
            return render(request, 'scholarship.html', context=context)
    form = QuestionFormForm()
    context = {'form': form}
    return render(request, 'scholarship.html', context=context)

@login_required(login_url='login')
@staff_member_required
def downloadResponse(request, formcode=None):
    
    if formcode !=None:
        response = HttpResponse(content_type='text/csv')
        responses = Response.objects.filter(form_id=formcode)
        writer = csv.writer(response)
        writer.writerow(['User', 'Submit Date', 'Answer1', 'Answer2', 'Answer3'])
        for r in responses:
            user = User.objects.get(id=r.user_id)
            writer.writerow([user, r.submitDate, r.answer1 ,r.answer2 , r.answer3])

        response['Content-Disposition'] = 'attachment; filename="response.csv"'
        return response     
    return render(request, 'download.html')