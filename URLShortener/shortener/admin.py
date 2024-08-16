from django.contrib import admin
from . import models, views

# Register your models here.
@admin.register(models.Urls)
class UrlAdmin(admin.ModelAdmin):
    list_display = ('id','ourl','gurl')
