from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('registration', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout'),
    path('welcome', views.welcome, name = 'welcome'),
]
