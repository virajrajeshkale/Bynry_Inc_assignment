# customer/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.customer_dashboard, name='customer_dashboard'),  # Customer Dashboard
    path('create-request/', views.create_request, name='create_request'),  # Create Service Request
]