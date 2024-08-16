from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('<str:gurl>/', views.redirect_url, name='redirect_url'),
]
