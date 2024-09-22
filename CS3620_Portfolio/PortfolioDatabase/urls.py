from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('hobbies/', views.hobbies, name="hobbies"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('contact/', views.contact, name="contact"),
]