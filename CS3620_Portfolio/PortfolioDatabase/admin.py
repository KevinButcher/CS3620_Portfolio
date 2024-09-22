from django.contrib import admin
from .models import Hobby
from .models import Portfolio

# Register your models here.


admin.site.register(Hobby)
admin.site.register(Portfolio)