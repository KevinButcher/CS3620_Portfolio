from django.shortcuts import render
from django.http import HttpResponse
from .models import Hobby
from .models import Portfolio

# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome!\n</h1>" + "My name is Kevin Butcher. I am in my senior"
                        "\nyear at Weber State University. I've attended school full time for"
                        "\nthree years now while also working a full time job (sadly, unrelated" 
                        "\nto my major). I am also  married married with a 7 year old son.")

def  hobbies(request):
    hobby_list = Hobby.objects.all()
    return HttpResponse(hobby_list)

def portfolio(request):
    portfolio_list = Portfolio.objects.all()
    return HttpResponse(portfolio_list)

def contact(request):
    return HttpResponse("Contact me: kevinbutcher@mail.weber.edu")

