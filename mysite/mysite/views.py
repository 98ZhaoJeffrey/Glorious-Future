from django.shortcuts import render

def index(request):
    """Route for our homepage
        
    Parameters:
    
    None

    Returns:

    HTML page
    """
    return render(request, 'base.html')

def about(request):
    """Route for our about page
        
    Parameters:
    
    None

    Returns:

    HTML page
    """
    return render(request, 'about.html')

def handle404Page(request):
    """Route for our about page
        
    Parameters:
    
    None

    Returns:

    HTML page
    """
    context={}
    response = render(request, "pages/errors/404.html", context=context)
    response.status_code = 404
    return response