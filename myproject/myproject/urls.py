# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls')),
    path('accounts/', include('accounts.urls')),  # ← bu bor bo‘lishi kerak
    path('', include('myapp.urls')),
]
