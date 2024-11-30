# customer/admin.py
from django.contrib import admin
from .models import ServiceRequest

class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'request_type', 'status', 'created_at')  # Fields to display in the list view
    list_filter = ('status', 'request_type', 'user')  # Filters for the sidebar
    search_fields = ('description',)  # Searchable fields
    ordering = ('-created_at',)  # Default ordering by creation date (newest first)

# Register the ServiceRequest model with the custom admin class
admin.site.register(ServiceRequest, ServiceRequestAdmin)
