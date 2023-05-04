from django.contrib import admin
from .models import AppImgs


class ImgAppAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'image')
    list_display_links = ('image')
    list_filters = ('title',"slug")
    list_editable = ('title', 'imagem')

admin.site.register(AppImgs)
