
from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # The home page URL
    path('auth/', include('base.urls')),
    path('customer/', include('customer.urls')),
    path('support/', include('support.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)