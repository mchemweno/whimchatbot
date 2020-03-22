from django.urls import path
from . import views

urlpatterns = [
    path('wikipedia/', views.WhatsappBot)
]
