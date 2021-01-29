from django.shortcuts import render

def index(request):
    """
    Route for the index page

    **Template:**
        :template:`base.html`

    """
    return render(request, 'base.html')

def about(request):
    """
    Route for the about page

    **Template:**
        :template:`about.html`

    """
    return render(request, 'about.html')

def handle404Page(request):
    """
    Route everything that 404s here

    **Template:**
        :template:`404.html`

    """
    context={}
    response = render(request, "pages/errors/404.html", context=context)
    response.status_code = 404
    return response