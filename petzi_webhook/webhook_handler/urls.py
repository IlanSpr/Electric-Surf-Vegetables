from django.urls import path
from . import views

urlpatterns = [
    path('petzi_webhook/', views.webhook, name='petzi_webhook_handler'),
]
