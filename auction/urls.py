from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='auction-home'),
    path('about/', views.about, name='auction-about'),
]
