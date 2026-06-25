from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request: http request's object
def landing_page(request):
    return HttpResponse("<h1>Welcome to Django Workshop</h1>")

def about_page(request):
    return HttpResponse("<h1>About Page</h1>")

def faq_page(request):
    return HttpResponse("<h1>FAQ Page</h1>")