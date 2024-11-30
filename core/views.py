from django.shortcuts import render

def home(request):
    """
    Render the landing page (home.html)
    """
    return render(request, 'home.html')