from django.contrib import admin

# Register your models here.

from .models import ItemsModel

class ItemModel(admin.ModelAdmin):
    list_display=['id', 'name','price']
    search_fields=['id', 'name']
    list_per_page: 2 

admin.site.register(ItemsModel)