from django.urls import path
from . import views

urlpatterns = [
    path('petzi_webhook/', views.petzi_webhook_handler, name='petzi_webhook_handler'),
]