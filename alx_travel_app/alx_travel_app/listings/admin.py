from django.contrib import admin
from .models import Listing

# Register your models here.

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'price_per_night', 'host', 'created_at']
    list_filter = ['location', 'created_at', 'host']
    search_fields = ['title', 'location', 'description']
    ordering = ['-created_at']
