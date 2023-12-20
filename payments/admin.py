from django.contrib import admin

from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price', 'currency']
    list_display_links = ['id', 'name']
    list_editable = ['price',]
    search_fields = ['name', 'description', 'price']
