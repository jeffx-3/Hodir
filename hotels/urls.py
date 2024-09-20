from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('search/', views.search_restaurants , name='search_restaurants'),
]
