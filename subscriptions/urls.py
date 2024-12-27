from django.urls import path
from .views import save_email, health_check

urlpatterns = [
    path('save_email/', save_email, name='save_email'),
    path('health/', health_check, name='health_check'),
]
