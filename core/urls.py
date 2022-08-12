from django.urls import path, include
from .views import HomeView
from core import views

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('register', views.register_request, name='register')
]
