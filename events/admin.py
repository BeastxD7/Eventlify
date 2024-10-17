from django.contrib import admin
from .models import Event

@admin.register(Event)  # Ensure this line is only present once
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'date', 'time', 'location', 'price')
    search_fields = ('name', 'category')
    list_filter = ('category',)  # Add a filter for category


