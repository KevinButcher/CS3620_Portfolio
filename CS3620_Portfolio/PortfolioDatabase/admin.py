from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Hobby, Contact, Portfolio, Tag

# Register your models here.

class AdminVideo(AdminVideoMixin, admin.ModelAdmin):
    pass

# admin.site.register(Hobby)
admin.site.register(Portfolio, AdminVideo)
admin.site.register(Contact)
admin.site.register(Tag)