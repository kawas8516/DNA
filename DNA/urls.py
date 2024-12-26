from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from subscriptions.views import index
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('api/', include('subscriptions.urls')),  # For the email subscription API
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
