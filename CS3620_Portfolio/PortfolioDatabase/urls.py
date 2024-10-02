from . import views
from django.urls import path

app_name = 'PortfolioDatabase'
urlpatterns = [
    # /PortfolioDatabase
    path('', views.index, name="index"),
    # /PortfolioDatabase/1 /PortfolioDatabase/2
    path('portfolio/<int:Portfolio_id>', views.portfolioDetail, name="portfolioDetail"),
    path('hobby/<int:Hobby_id>', views.hobbyDetail, name="hobbyDetail"),
    path('hobbies/', views.hobbies, name="hobbies"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('contact/', views.contact, name="contact"),
]