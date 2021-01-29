from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Q
from post.models import *

# Create your views here.

"""
test user
u = User.objects.create_user(username="testname", first_name="firsttest", last_name="lasttest", email="test@email.com", location="Toronto")
pass = testpassword
"""

def signup(request):
    """
    Allows the user to signup for the website service as either a student or an organization

    **Template:**

    :template:`registration/signup.html`

    """
    if request.user.is_authenticated:
        return redirect('index')
    else:  
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        form = UserRegisterForm()
        return render(request, 'registration/signup.html', {'form': form})

@login_required(login_url='login')

def logout(request):
    """
    Check
    **Redirect:**

    :`route:login`

    """
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request):
    """
    Returns the profile page. If a student, shows how much they could save, if organization, allows them to download the responses

    **Redirect:**

    :template:`student_profile.html or organization_profile.html`

    """

    if(request.user.is_staff):
        #get all posts they had and let them download those results
        posts = Post.objects.filter(organization_id=request.user.id)
        context={
            'posts':posts,
            'user': request.user,
            'count': posts.count(),
        }
        return render(request, 'organization_profile.html', context=context)
    userReponses = Response.objects.filter(user_id=request.user.id)
    scholarshipTotal = 0
    for response in userReponses:
        scholarshipTotal += Post.objects.filter(Q(link__icontains=response.form_id))[0].value

    context = {
        'user': request.user,
        'count': userReponses.count(),
        'total': scholarshipTotal
    }
    return render(request, 'student_profile.html', context=context)