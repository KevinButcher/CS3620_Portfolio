from django.contrib import admin
from .models import Hobby, Contact, Portfolio

# Register your models here.


admin.site.register(Hobby)
admin.site.register(Portfolio)
admin.site.register(Contact)