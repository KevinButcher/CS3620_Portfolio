from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Hobby, Portfolio
from django.template import loader
from .forms import PortfolioForm, ContactForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    context = {
        "intro": "My name is Kevin Butcher. I am in my senior"
                        " year at Weber State University. I've attended school full time for"
                        " three years now while also working a full time job (sadly, unrelated"
                        " to my major). I am also married with a 7 year old son."
    }
    return render(request, 'PortfolioDatabase/index.html', context)
    #return HttpResponse("<h1>Welcome!\n</h1>" + "My name is Kevin Butcher. I am in my senior"
                        #"\nyear at Weber State University. I've attended school full time for"
                        #"\nthree years now while also working a full time job (sadly, unrelated" 
                        #"\nto my major). I am also  married married with a 7 year old son.")

# def  hobbies(request):
#     hobby_list = Hobby.objects.all()
#     context = {
#         'hobby_list': hobby_list
#     }
#     return render(request, 'PortfolioDatabase/hobbies.html', context)
#     #return HttpResponse(hobby_list)

def portfolio(request):
    portfolio_list = Portfolio.objects.all()
    context = {
        'portfolio_list': portfolio_list
    }
    return render(request, 'PortfolioDatabase/portfolio.html', context)
    #return HttpResponse(portfolio_list)

def contact(request):
    context = {
        "contact": "Contact me @ kevinbutcher@mail.weber.edu"
    }
    return render(request, 'PortfolioDatabase/contact.html', context)
    #return HttpResponse("Contact me: kevinbutcher@mail.weber.edu")

# def hobbyDetail(request, Hobby_id):
#     hobby = Hobby.objects.get(pk=Hobby_id)
#     context = {
#         'hobby': hobby,
#     }
#     return render(request, 'PortfolioDatabase/detail.html', context)

def portfolioDetail(request, Portfolio_id):
    portfolio = Portfolio.objects.get(pk=Portfolio_id)
    context = {
        'portfolio': portfolio,
    }
    return render(request, 'PortfolioDatabase/detail.html', context)

def contactMe(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contactName = form.cleaned_data.get('contact_name')
            messages.success(request, f'Thanks for reaching out {contactName}! Your message has been saved.')
            form.save()
            return redirect('PortfolioDatabase:contact')
    else:
        form = ContactForm()
    
    return render(request, 'PortfolioDatabase/contact-form.html', {'form': form})

@login_required
def createPortfolio(request):
    form = PortfolioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('PortfolioDatabase:portfolio')
    
    
    return render(request, 'PortfolioDatabase/portfolio-form.html', {'form': form})

# @login_required
# def createHobby(request):
#     form = HobbyForm(request.POST or None)

#     if form.is_valid():
#         form.save()
#         return redirect('PortfolioDatabase:hobbies')
    
#     return render(request, 'PortfolioDatabase/hobby-form.html', {'form': form})

@login_required
def updatePortfolio(request, Portfolio_id):
    portfolio = Portfolio.objects.get(pk=Portfolio_id)
    form = PortfolioForm(request.POST or None, instance=portfolio)

    if form.is_valid():
        form.save()
        return redirect('PortfolioDatabase:portfolio')
    
    return render(request, 'PortfolioDatabase/portfolio-form.html', {'form': form, 'portfolio': portfolio})

# @login_required
# def updateHobby(request, Hobby_id):
#     hobby = Hobby.objects.get(pk = Hobby_id)
#     form = HobbyForm(request.POST or None, instance=hobby)

#     if form.is_valid():
#         form.save()
#         return redirect('PortfolioDatabase:hobbies')
    
#     return render(request, 'PortfolioDatabase/hobby-form.html', {'form': form, 'hobby': hobby})

@login_required
def deletePortfolio(request, Portfolio_id):
    portfolio = Portfolio.objects.get(pk=Portfolio_id)

    if request.method == 'POST':
        portfolio.delete()
        return redirect('PortfolioDatabase:portfolio')
    
    return render(request, 'PortfolioDatabase/item-delete.html', {'portfolio': portfolio})

# @login_required
# def deleteHobby(request, Hobby_id):
#     hobby = Hobby.objects.get(pk=Hobby_id)

#     if request.method == 'POST':
#         hobby.delete()
#         return redirect('PortfolioDatabase:hobbies')
    
#     return render(request, 'PortfolioDatabase/item-delete.html', {'hobby': hobby})

