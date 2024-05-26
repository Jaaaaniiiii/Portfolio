from django.urls import path
from portofolio import views

urlpatterns = [
    path('', views.home, name='home'),
]