from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

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
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request):
    if(request.user.is_staff):
        #gett all posts they had and let them download those results, add delete as well
        pass
    return redirect('about')