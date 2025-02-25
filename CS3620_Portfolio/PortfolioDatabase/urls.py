from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

app_name = 'PortfolioDatabase'
urlpatterns = [
    # /PortfolioDatabase
    path('', views.index, name="index"),
    # /PortfolioDatabase/1 /PortfolioDatabase/2
    path('portfolio/<int:Portfolio_id>', views.portfolioDetail, name="portfolioDetail"),
    # path('hobby/<int:Hobby_id>', views.hobbyDetail, name="hobbyDetail"),
    # path('hobbies/', views.hobbies, name="hobbies"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('contact/', views.contact, name="contact"),
    path('addproject', views.createPortfolio, name="createPortfolio"),
    # path('addhobby', views.createHobby, name="createHobby"),
    path('updateproject/<int:Portfolio_id>', views.updatePortfolio, name="updatePortfolio"),
    # path('updatehobby/<int:Hobby_id>', views.updateHobby, name="updateHobby"),
    path('deleteproject/<int:Portfolio_id>', views.deletePortfolio, name="deletePortfolio"),
    # path('deletehobby/<int:Hobby_id>', views.deleteHobby, name="deleteHobby"),
    path('contactme/', views.contactMe, name="contactMe"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)