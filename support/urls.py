# support/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.support_dashboard, name='support_dashboard'),  # Support Dashboard
    path('assign-request/<int:request_id>/', views.assign_request, name='assign_request'),  # Assign/Update Request
]
