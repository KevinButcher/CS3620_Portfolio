"""
URL configuration for CS3620_Portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Users import views as userViews
from django.contrib.auth import views as authenticationViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("PortfolioDatabase/", include("PortfolioDatabase.urls")),
    path('register/', userViews.register, name='register'),
    path('login/', authenticationViews.LoginView.as_view(template_name='Users/login.html'), name='login'),
    path('logout/', authenticationViews.LogoutView.as_view(template_name='Users/logout.html'), name='logout'),
    path('profile/', userViews.profilepage, name='profile'),
]

urlpatterns += [

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)