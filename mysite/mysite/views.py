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