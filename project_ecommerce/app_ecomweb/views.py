from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request: http request's object
def landing_page(request):
    context = {
        "title": "Django Workshop",
        "subtitle": "NCIT | BCA",
        "message": "Welcome to Django Workshop. This is the landing page of the project.",
        "year": 2026
    }
    return render(request, "landing.html",context)

def about_page(request):
    context = {
        "title": "About Us",
        "products":["Books", "Pen", "Product 3"],
    }
    return render(request, "pages/about.html",context)

def faq_page(request):
    return render(request, "pages/faq.html")