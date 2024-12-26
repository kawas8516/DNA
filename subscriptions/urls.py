
from django.urls import path
from .views import save_email

urlpatterns = [
    path('save_email/', save_email, name='save_email'),
]
